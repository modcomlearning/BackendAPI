 # THIS IS AN API FOR Ecommerce Backend
from flask import *

# Create the Flask application instance
app = Flask(__name__)


# setup file upload
import os
app.config['UPLOAD_FOLDER'] = 'static/images'
import pymysql


# Define the sign up Route/Endpoint
@app.route('/api/signup', methods = ['POST'])
def signup():
    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
     
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


import pymysql.cursors
@app.route('/api/signin', methods = ['POST'])
def signin():
        # Extract POST data
        email = request.form['email']
        password = request.form['password']
        
        # Connect to DB
        connection = pymysql.connect(host='localhost', user='root',
                                        password='',database='BackendAPI')
        
        # Create a cursor to return results a dictionary, initialize connection
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        # Do select SQL,test ghis SQL first in phpmyadmin
        sql = "select * from users where email = %s and password = %s"
        # Prepare data to replace placeholders %s
        data = (email, password)
        # use cursor to execute SQL providing the data to replace placeholders
        cursor.execute(sql,data)
        
        #  Check how many rows are found
        count = cursor.rowcount
        # If rows a zero, Invalid Credentials - No user Found
        if count == 0:
            return jsonify({"message": "Login Failed"})
        else:
            # else there is a user, return a message to say login success and all user details,fetchone gets the logged in user details
            user = cursor.fetchone()
            
            # Return login success message with user details as a dictionary
            return jsonify({"message": "Login Success", "user": user})
         


# Define the Add Product Route/Endpoint
@app.route('/api/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        # Extract POST Data
        product_name = request.form['product_name']
        product_description = request.form['product_description']
        product_cost = request.form['product_cost']
        # Extract image data
        photo = request.files['product_photo']
        # Get the image file name
        filename = photo.filename
        # SPecify where the image will be saved (in static Folder) - Image Path
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Save your image
        photo.save(photo_path)

        # Connect to DB
        connection = pymysql.connect(host='localhost', user='root',
                                        password='',database='BackendAPI')
        # Prepare and execute the insert query
        cursor = connection.cursor()
        cursor.execute('INSERT INTO product_details (product_name, product_description, product_cost, product_photo) '
                    'VALUES (%s, %s, %s, %s)',
                    (product_name, product_description, product_cost,  filename))

        # Commit the changes to the database
        connection.commit()
        # Return success message in Dictionary Format
        return jsonify({"success": "Product details added successfully"})




# Define the Get Product Details Route/Endpoint
import pymysql.cursors
@app.route('/api/get_product_details', methods=['GET'])
def get_product_details():

    # Connect to the database with DictCursor for direct dictionary results
    connection = pymysql.connect(host='localhost', user='root',
                                        password='',database='BackendAPI')

    # Create a cursor object and fetch all products details from the products_details table
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM product_details')
    product_details = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Return the products details directly as a dictionay - JSON
    return jsonify(product_details)



# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
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