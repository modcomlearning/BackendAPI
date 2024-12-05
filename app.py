from flask import *

# Create the Flask application instance
app = Flask(__name__)
import pymysql

# Define the sign up Endpoint
@app.route('/api/signup', methods = ['POST'])
def signup():
    if request.method =='POST':
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']
     
        # COnnect to DB
        connection = pymysql.connect(host='localhost', user='root',
                                        password='',database='ShopBackendAPI')
        # Do insert query
        cursor = connection.cursor()
        cursor.execute('insert into users(username,email,password)values(%s,%s,%s)',
                            (username, email, password))
        
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
                                        password='',database='ShopBackendAPI')
         
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
         



# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)