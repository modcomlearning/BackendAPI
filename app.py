from flask import *

# Create the Flask application instance
app = Flask(__name__)



# setup file upload
import os
app.config['UPLOAD_FOLDER'] = 'static/images'
import pymysql


# Define the sign up Endpoint
@app.route('/api/signup', methods = ['POST'])
def signup():
    if request.method =='POST':
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']
        phone = data['phone']
     
        # COnnect to DB
        connection = pymysql.connect(host='localhost', user='root',
                                        password='',database='BackendAPI')
        # Do insert query
        cursor = connection.cursor()
        cursor.execute('insert into users(username,email,password, phone)values(%s,%s,%s,%s)',
                            (username, email, password, phone))
        
        # we need to make a commit to changes to dbase
        connection.commit()
        return jsonify({"success": "Thank you for Joining"})


# Define the sign in Endpoint
import pymysql.cursors
@app.route('/api/signin', methods = ['POST'])
def signin():
    if request.method == 'POST':
         data = request.json
         email = data['email']
         password = data['password']  
         
         # Connect to DB
         connection = pymysql.connect(host='localhost', user='root',
                                        password='',database='BackendAPI')
         
         cursor = connection.cursor(pymysql.cursors.DictCursor)
         sql = "select * from users where email = %s and password = %s"
         data = (email, password)
         cursor.execute(sql,data)
         
        #  Check how many rows are found
         count = cursor.rowcount
         # If rows a zero, Invalid Credentials
         if count == 0:
             return jsonify({"message": "Login Failed"})
         else:
             # else there is a user, return a message to say login success and all user details
             user = cursor.fetchone()
             
             # Return login success message with user details as a tuple
             return jsonify({"message": "Login success", "user": user})
         


# Define the Add Land Endpoint
@app.route('/api/add_land', methods=['POST'])
def add_land():
    if request.method == 'POST':
        # data = request.json
        land_description = request.form['land_description']
        land_location = request.form['land_location']
        land_cost = request.form['land_cost']
        land_size = request.form['land_size']
        land_owner = request.form['land_owner']
        plot_no = request.form['plot_no']
        photo = request.files['land_photo']
        filename = photo.filename
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)
     
        # Connect to DB
        connection = pymysql.connect(host='localhost', user='root',
                                        password='', database='BackendAPI')
        # Prepare and execute the insert query
        cursor = connection.cursor()
        cursor.execute('INSERT INTO land_details (land_description, land_location, land_cost, land_size, land_owner, plot_no, land_photo) '
                       'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (land_description, land_location, land_cost, land_size, land_owner, plot_no, filename))
        
        # Commit the changes to the database
        connection.commit()
        return jsonify({"success": "Land details added successfully"})




# Define the Get Land Details Endpoint
@app.route('/api/get_land_details', methods=['GET'])
def get_land_details():
    # Connect to the database with DictCursor for direct dictionary results
    connection = pymysql.connect(host='localhost', user='root',
                                    password='', database='BackendAPI')
    
    # Create a cursor object and fetch all land details from the land_details table
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM land_details')
    land_details = cursor.fetchall()
    
    # Close the database connection
    connection.close()
    
    # Return the land details directly as JSON
    return jsonify(land_details)



# Mpesa Payment Route 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        data = request.json
        phone = data['phone']
        amount =data['amount']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})
    
# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)