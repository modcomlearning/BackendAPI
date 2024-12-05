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

    else: # this means POST was not used, show the signup template
        return jsonify({"error": "Registration Failed, Try again later"})



# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)