### A Full-Stack Lands Management System (Buy or Sell) with Flask, MySQL, React JS, and MPESA Payment Integration

This is a full-stack Land (Selling and Buying System) management application built with Flask for the backend, MySQL for the database, and React JS for the frontend. The application allows users to register, log in, browse products, and make payments via MPESA, a popular mobile money service. Here’s how each component functions in the system.

The Flask backend serves as the API layer, providing several key functions:

2. Backend (Flask)

    User Authentication: The backend handles user registration and login, storing users’ details (like emails and hashed passwords) in the MySQL database.
     
    Land Management: The application retrieves land details from the MySQL database, including land location, price, owner details, plot No, etc and send it to the frontend for buyers to see the details. It also handles user signup, signin, land addition, land search and view, and payment processing.

    MPESA Payment: When users are ready to pay, the backend interacts with the MPESA API to initiate and confirm mobile payments. Once the payment is complete, the backend updates product stock if necessary.

3. Database (MySQL)

The database stores the essential information for the application:

    Users Table: Contains user details (name, email, password).
    Lands Table: Stores land details like name, description, price, and location.

4. MPESA Payment Integration

    Payment Initiation: After selecting products, the user is asked to pay via MPESA. The backend sends a request to MPESA API with payment details.
    Payment Confirmation: MPESA sends a callback to confirm whether the payment was successful. If successful, the backend updates product availability and notifies the user.



Technologies Used

Frontend: React JS for building the user interface and interacting with the Flask API.
Backend: Flask for handling user authentication, managing land, and processing MPESA payments.
Database: MySQL for storing user and doctors information.
Payment: MPESA API for handling mobile money payments.



## Step 1: Creating MySQL Database.
To build a shopping system with Flask and MySQL, the first step is to create a MySQL database. The database will store important data such as user information (names, emails, passwords) and product details (names, descriptions, prices, quantities).

Here’s a brief explanation of the tools involved:

What is XAMPP?
XAMPP is a software package that provides a simple way to set up a local web server environment. It includes:

    Apache: A web server software to serve your websites.
    MySQL: A popular database management system used to store data.
To Install XAMPP check these Links
https://www.apachefriends.org/download.html


After XAMPP installation, Create a Database named "ShopBackendAPI" and create two tables below are SQL for creating the Tables.

Users Table

        CREATE TABLE users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            phone VARCHAR(50)
        );




![Alt text](image.png)        


Lands Table
       
      CREATE TABLE land_details (
            land_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each land entry
            land_description TEXT,                   -- Description of the land
            land_location VARCHAR(255),              -- Location of the land
            land_cost INT,                           -- Cost of the land as an integer (no decimal places)
            land_size VARCHAR(50),                   -- Size of the land as a string (e.g., in square feet, square meters)
            land_owner VARCHAR(255),                 -- Name of the land owner
            plot_no VARCHAR(50)                      -- Plot number of the land
        );

![Alt text](image-5.png)


## Step 2: API Creation Development using Flask_restful.
What is an API?

API stands for Application Programming Interface. It is a set of rules and protocols that allows different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information.

In the context of web development:

    An API allows a frontend (like a website or mobile app) to interact with a backend server.
    The backend exposes various endpoints that the frontend can send requests to (like fetching product data, registering a user, or processing payments).
    APIs typically use HTTP methods like GET (retrieve data), POST (send data), PUT (update data), and DELETE (remove data).

For example, our shopping app will have an API to handle user registration, login, and retrieving land listings etc.


## Step 3: Setting Up Flask restful
Install Flask if you haven't already:
   
     pip install flask


Create a New Folder named ShopBackendAPI, inside this folder, create below flask app structure.
Inside app.py write below code.

        from flask import *

        # Create the Flask application instance
        app = Flask(__name__)

        # Define a simple route
        @app.route('/signup')
        def signup():
            return "Welcome to sign Up route!"

        # Run the app if this file is executed directly
        if __name__ == '__main__':
            app.run(debug=True)



Test this code in Insomnia -  Insomnia is a popular, open-source API client used for testing, debugging, and interacting with RESTful APIs.

Output

![Alt text](image-2.png)


Done, we have already done and tested our first API



## Step 4: Create a SignUp API.
When you refer to signup, it typically means the process where users register their details to create an account on a website or application. During the signup process, users provide certain information (e.g., username, email, password) that is stored in the system to uniquely identify them and allow them to access features of the application.

First install pymysql

    pip install pymysql

Then import pymysql like below.

    import pymysql

An endpoint in web development and APIs is a specific URL that allows you to access or interact with the API.
Read more with an Example in Below Link
https://justpaste.it/fznuk

Check what is a JSON Object   > https://justpaste.it/gxpd9

Update your /api/signup route as follows.
Below is the updated app.py

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
                                                password='',database='BackendAPI')
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


RUn your flask app, The above api can be accessed through  http://127.0.0.1:5000/api/signup   ,  http://127.0.0.1:5000/being the base url and api/signup  is the specific endpoints your API resource.


Test above api in Insomnia.
NB: In insomnia create a New Folder to store requests (Also rename your requests).
In below requests we use http://127.0.0.1:5000/api/signup as the endpoint, we use POST and the body is exactly as they are defined in our /api/signup Endpoint request variables.


JSON Body

    {
        "username": "Tom",
        "email": "tom@gmail.com",
        "password": "123456",
        "phone": "0755XXXXXX"
    }
Output

![Alt text](image-9.png)


## Step 5: Create a Signin API.
Below API endpoint will allow users to Signin using credentials provided in /api/signup in Step 4 above. Update your app.py by adding an /api/signin route as shown below.

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
                return jsonify({"message": "Login Success", "user": user})


NB: Above we imported import pymysql.cursors  and used in the cursor cursor = connection.cursor(pymysql.cursors.DictCursor), this will help in returning the user details in a Key Value representation.

Your complete app.py now looks like below.

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
                                                password='',database='BackendAPI')
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
                


        # Run the app if this file is executed directly
        if __name__ == '__main__':
            app.run(debug=True)




Test the /ap/signin in Insomnia
JSON Body

    {
        "email": "tom@gmail.com",
        "password": "123456"
    }



Output

![Alt text](image-4.png)


## Step 6: Create a Land upload API.
This endpoint will be used by users in uploading their land details
in app.py add below route to create the API Endpoint

    # Define the Add Land Endpoint
    @app.route('/api/add_land', methods=['POST'])
    def add_land():
        if request.method == 'POST':
            data = request.json
            land_description = data['land_description']
            land_location = data['land_location']
            land_cost = data['land_cost']
            land_size = data['land_size']
            land_owner = data['land_owner']
            plot_no = data['plot_no']
        
            # Connect to DB
            connection = pymysql.connect(host='localhost', user='root',
                                            password='', database='ShopBackendAPI')
            # Prepare and execute the insert query
            cursor = connection.cursor()
            cursor.execute('INSERT INTO land_details (land_description, land_location, land_cost, land_size, land_owner, plot_no) '
                        'VALUES (%s, %s, %s, %s, %s, %s)',
                        (land_description, land_location, land_cost, land_size, land_owner, plot_no))
            
            # Commit the changes to the database
            connection.commit()
            return jsonify({"success": "Land details added successfully"})


Test above in insomnia
JSON Body
    
     {
        "land_description": "A great farm for growing maize, very warm and fertile",
        "land_location": "Kahawa, Nairobi, Kenya",
        "land_cost": 750000,
        "land_size": "70000 sq ft",
        "land_owner": "John Dere",
        "plot_no": "NB9876"
     }

![Alt text](image-6.png)

## Step 7: Create a View Available Lands  API.
This endpoint will be used by users to View Posted lands
In app.py add below route to create the API Endpoint.

Check more JSON Array > https://justpaste.it/gxpd9

    # Define the Get Land Details Endpoint
    @app.route('/api/get_land_details', methods=['GET'])
    def get_land_details():
        # Connect to the database with DictCursor for direct dictionary results
        connection = pymysql.connect(host='localhost', user='root',
                                        password='', database='ShopBackendAPI')
        
        # Create a cursor object and fetch all land details from the land_details table
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM land_details')
        land_details = cursor.fetchall()
        
        # Close the database connection
        connection.close()
        
        # Return the land details directly as JSON
        return jsonify(land_details)



Test in Insmnia
In below image shows a JSON Array showing several lands displayed
Output

![Alt text](image-7.png)


## Step 8: Making an MPESA Payment API.
The API Endpoint below will be used for any payment to be done in our land Management System.
We will use MPESA Daraja Intergration. Please check https://developer.safaricom.co.ke/


NB: you will need to install requests if not already installed.

    pip install requests

In app.py add below code

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


Test in Insomnia

JSON Body

    {
        "phone":"254745131917",
        "amount": "1"
    }

Output

![Alt text](image-8.png)

Your Final app.py looks like below

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
            



    # Define the Add Land Endpoint
    @app.route('/api/add_land', methods=['POST'])
    def add_land():
        if request.method == 'POST':
            data = request.json
            land_description = data['land_description']
            land_location = data['land_location']
            land_cost = data['land_cost']
            land_size = data['land_size']
            land_owner = data['land_owner']
            plot_no = data['plot_no']
        
            # Connect to DB
            connection = pymysql.connect(host='localhost', user='root',
                                            password='', database='ShopBackendAPI')
            # Prepare and execute the insert query
            cursor = connection.cursor()
            cursor.execute('INSERT INTO land_details (land_description, land_location, land_cost, land_size, land_owner, plot_no) '
                        'VALUES (%s, %s, %s, %s, %s, %s)',
                        (land_description, land_location, land_cost, land_size, land_owner, plot_no))
            
            # Commit the changes to the database
            connection.commit()
            return jsonify({"success": "Land details added successfully"})




    # Define the Get Land Details Endpoint
    @app.route('/api/get_land_details', methods=['GET'])
    def get_land_details():
        # Connect to the database with DictCursor for direct dictionary results
        connection = pymysql.connect(host='localhost', user='root',
                                        password='', database='ShopBackendAPI')
        
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


In this Github repo, we created an API for Land Management System for Posting and buying Land,
The application provides an API to signup, signin, add_land, get_lands_details and MPESA payment integration. This API creates the Back - End of our full-stack application.

Above API will be accessed in the Front - End (User Side) by Reacct JS and Android Application.
Next is Front - End Development using React JS and later Android Apps.

Happy Coding!