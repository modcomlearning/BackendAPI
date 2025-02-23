### A Full-Stack E-commerce (Buy or Sell Products) with Flask, MySQL, React JS, and MPESA Payment Integration
<b>Introduction</b> <br/>
In this Module, You will be creating a Complete Full-Stack commerce Web Application(Selling and Buying System)  built with Flask for the backend, MySQL for the database, and React JS for the frontend.
We will Call This Application <h3><b>SOKOGARDEN</b></h3>
<br>
This E-Commerce Web Application is a website where people can buy and sell products online, The application is inspired by growing web applications such Jumia, Kilimall, Alibaba, and Jiji. It Allows users to create account(Signup), Sign in Sell Products, Buy Products, Browse Products, Make MPESA Payment etc.
<br><br>
DEMO the Web Application<br>
Link : https://sokogarden.vercel.app  <br>

The Flask backend serves as the Backend layer, providing several key functions:

2. Backend (Flask)

    User Authentication: The backend handles user registration and login, storing users’ details (like emails and passwords) in the MySQL database.
     
    Product Management: The application retrieves product details from the MySQL database, including product_name, description , cost, photo etc and send it to the frontend for buyers to see the details. It also handles user signup, signin, product addition, product search and view, and payment processing.

    MPESA Payment: When users are ready to pay, the backend interacts with the MPESA API to initiate and confirm mobile payments.

3. Database (MySQL)

The database stores the essential information for the application:

Users Table: Contains user details (name, email, password).
Product Table: Stores products details like name, description, price, and photo.
<br>

4. MPESA Payment Integration

    Payment Initiation: After selecting products, the user is asked to pay via MPESA. The backend sends a request to MPESA API with payment details.

<br>
<b>Technologies Used</b>
Frontend: React JS for building the user interface and interacting with the Flask API.
Backend: Flask for handling user authentication, managing producrs, and processing MPESA payments.
Database: MySQL for storing user and doctors information.
Payment: MPESA API for handling mobile money payments.

### THIS REPO CREATES THE BACKEND ONLY
## Step 1: Creating MySQL Database.
To build a shopping system with Flask and MySQL, the first step is to create a MySQL database. The database will store important data such as user information (names, emails, passwords) and product details (names, descriptions, prices, quantities).
<br/>
Please check our Book4 for SQL Database Setup and Guide.

<br/>
<b><h3>NB: Use your Existing Database</h3></b>
<br/>

In Your Database Create below two tables; <br/>
1. users  -  used to store our system users<br/>
2. product_details - used to store product details/information 
<br/>


<b>Users Table</b>

        CREATE TABLE users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            phone VARCHAR(50)
        );


![Alt text](image.png)        


<b>Products Table</b>
       
       CREATE TABLE product_details (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            product_description TEXT,
            product_cost INT,
            product_photo VARCHAR(255)
        );


![alt text](image-16.png)

<br/>
Now that we have a Database with Tables, Next step is to create a Python Application to interact with this Database.
<br/>

## Step 1-1: Flask Framework

Flask is a popular web framework for building web applications in Python. It's designed to be simple, lightweight, and flexible, making it a great choice for developers who are learning web development. Here's an introduction to Flask.

<b>Key Features of Flask: </b>

<b>Easy to Use:</b> Flask is friendly due to its design and minimal setup. You can start building a web application with just a few lines of code. Flask is a good choice for backend development when creating advanced applications.

<b>Python-Based:</b> Since Flask is a Python framework, if you are familiar with Python, you will find it relatively easy to get started. Flask allows you to focus on building the logic and features of your app rather than dealing with complex configurations.

<b>Routing:</b> One of the most important features of Flask is routing, which allows you to map specific URLs to Python functions. For example, you can define a route for your homepage (/), and when someone visits your website, Flask will call the corresponding function to show the page.

<b>Development Server:</b> Flask comes with a built-in development server that makes testing and debugging applications easier. It automatically reloads when you make changes to the code.

<b>Extensible:</b> Flask can be extended with many plugins to handle more complex tasks, such as database integration (using SQLAlchemy), form validation, authentication, and more.

<b>Security: </b> It provides many tools and best practices that you can use to build secure web applications.

<b>Popularity: </b> Flask is extremely popular and in high demand, largely due to its use of Python, one of the most widely used and loved programming languages in the world. Here’s why Flask’s popularity is growing, and why it's in demand:


<b>Conclusion</b>:
Flask is popular and in demand primarily due to its use of Python, one of the most loved and versatile programming languages. Its simplicity, flexibility, and ability to integrate well with modern tools have made it a go-to framework for developers building everything from simple web apps to advanced systems. Whether you're building APIs, microservices, or integrating machine learning models, Flask's growing popularity and demand in the tech industry make it an excellent choice for backend development.


## Step 2: API Creation Development using Flask
What is an API?

API stands for Application Programming Interface. It allows different software applications to communicate with each other. APIs define the functions to exchange information between back end and front end. <br>

API stands for Application Programming Interface:  <br>

<b>A (Application)</b> – A software program or system that performs specific tasks.<br>
<b>P (Programming) </b> – The process of writing code to create program .<br>
<b>I (Interface) </b> – A point of interaction that allows different applications to communicate with each other.<br>

<b>In the context of web development:</b> <br>
An API allows a frontend (like a website or mobile app) to interact with a backend server.
The backend exposes various links or endpoints that the frontend can send requests to (like fetching product data, registering a user, or processing payments).

![alt text](image-17.png)
<br>
In this Module we do the Backend using Python and SQL<br>
For example, our E-commerce Web Application will have an API to handle user registration, login, add  product and retrieving Products listings etc.  Lets Do it Practically!
<br/>


## Step 2.1: Setting Up Flask, Testing Routes
Install Flask module if you haven't installed already:
   
     pip install flask

Create a New Folder(Create a Class Folder for this Project), inside this folder, create a Python File named test.py. <br/>
In this File we first learn the fundamentals on how create and interact with API (Application Programming Interface). Then we will move to Step 3: Where we create our eCommerce API.

in test.py add this code
    
```python
from flask import *

# Create the Flask appl
app = Flask(__name__)
# Define a simple route/Endpoint
# the designated paths or endpoints in a web application that correspond to specific functions
@app.route('/api/home')
def home():
    return jsonify({"message":"Welcome to HOME API!"})

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```

<b>Explanation</b> <br/>
This code creates a basic Flask web application.<br/>
Routes: Paths or endpoints in a web application that correspond to specific functions

1. app = Flask(__name__): Initializes the Flask app.<br/>
2. @app.route('/api/home'): Defines a route for the /signup URL.<br/>
3. def home(): The function that returns the message "Welcome to sign Up API!" when the /api/home route is accessed. Each must be attached to a function to give a fuctionality<br/> The message returned uses jsonify to return response in form of a Key Value Pair (Dictionary)
4. if __name__ == '__main__': Ensures the app runs only when the script is executed directly, not when imported as a module.<br/>
5. app.run(debug=True): Starts the development server with debugging enabled.<br/><br/>

Test this code in Insomnia -  Insomnia is a popular, open-source API client used for testing, debugging, and interacting with APIs.
<br/>
The API running at http://127.0.0.1:5000/   <br/>
For us to access the Home Route we write it in this format http://127.0.0.1:5000/api/home <br>

Use http://127.0.0.1:5000/api/home  while Testing your API in insomnia, http://127.0.0.1:5000/api/home  is also known an endpoint since its the link we use to reach the API <br/>

NB: Insomnia we use GET  -  GET only retrieves data from a server.
<br>
There are two types of messages: requests sent by the client to trigger an action on the server, and responses, the answer that the server sends back as a response. 

![alt text](image-32.png)

<br>
Output

![alt text](image-34.png)

Done, we have tested our first API
![alt text](image-18.png)

In test.py add another endpoint  

```python
    from flask import *

    # Create the Flask appl
    app = Flask(__name__)
    # Define a simple route/Endpoint
    @app.route('/api/home')
    def home():
        return jsonify({"message":"Welcome to HOME API!"})


    # Define a another simple route/Endpoint
    @app.route('/api/products')
    def products():
        return jsonify({"message":"Welcome to PRODUCTS API!"})


    # Run the app if this file is executed directly
    if __name__ == '__main__':
        app.run(debug=True)
```

Use http://127.0.0.1:5000/api/products  while Testing your API in insomnia, http://127.0.0.1:5000/api/products  is also known an endpoint since its the link we use to reach the API <br/>

Output
![alt text](image-35.png)

<b>Students Practice</b> <br>
- Create a route/endpoint named /api/services </>
- Create a function for this route and return a message "Welcome to Our Services API" as Key Value Pair.
- Test this endpoint in Insomnia. NB: Create a new request in insomnia.
<br>

## Step 2.2: Posting variables Request to API and Get Responses
In this example we are going to send a request with two numbers to our API endpoint named /api/calc , the api will process, add the two numbers and return a response with an answer.
<br>

in test.py add the /api/calc Route/endpoint as shown below.

```python
    from flask import *

    # Create the Flask appl
    app = Flask(__name__)
    # Define a simple route/Endpoint
    @app.route('/api/home')
    def home():
        return jsonify({"message":"Welcome to HOME API!"})


    # Define a another simple route/Endpoint
    @app.route('/api/products')
    def products():
        return jsonify({"message":"Welcome to PRODUCTS API!"})

    # Define a another simple route/Endpoint
    @app.route('/api/calc', methods = ['POST'])
    def calc():
        if request.method == 'POST':
            number1 = request.form['number1']
            number2 = request.form['number2']
            sum = int(number1)  + int(number2)
            # Return a dictionary : Key - Value Pairs
            return jsonify({'Answer ': sum})
        

    # Run the app if this file is executed directly
    if __name__ == '__main__':
        app.run(debug=True)
```
<br>
This Flask route /api/calc handles POST requests. It takes two numbers from the form data (number1 and number2), converts them to integers, adds them, and returns the sum as a response.
<br>

<b>Test in Insomnia</b> <br/>
When testing Please choose POST as the method and Form Data to send post the two variables number1 and number2, see below on how to pick form data.

![alt text](image-36.png)

See below image on how to append data to the request, we append number1 and number2 with their respective values. 

The API endpoint we are using to access our calc is http://127.0.0.1:5000/api/calc

Output
![alt text](image-37.png)

## Step 3: Setting Up Flask App for Our eCommerce Web Application - Backend

In your class Folder, create a Python File named app.py. <br/>
In this File we create our API (Application Programming Interface)
<br/>
Inside app.py write below code.

```python
        from flask import *

        # Create the Flask application instance
        app = Flask(__name__)

        # Define a simple route/Endpoint
        @app.route('/api/signup')
        def signup():
            return "Welcome to sign Up API!"

        # Run the app if this file is executed directly
        if __name__ == '__main__':
            app.run(debug=True)
``` 
<br/><br/>
<b>Explanation</b> <br/>
This code creates a basic Flask web application.<br/>

1. app = Flask(__name__): Initializes the Flask app.<br/>
2. @app.route('/signup'): Defines a route for the /api/signup URL.<br/>
3. def signup(): The function that returns the message "Welcome to sign Up API!" when the /signup route is accessed.<br/>
4. if __name__ == '__main__': Ensures the app runs only when the script is executed directly, in app.py, also specifies that this is the main application<br/>
5. app.run(debug=True): Starts the development server with debugging enabled.(debugging mode helps you fix exceptions when incase they arise in your code)<br/><br/>


Test this code in Insomnia -  Insomnia is a popular, open-source API client used for testing, debugging, and interacting with APIs.
<br/>
The API running at http://127.0.0.1:5000/   <br/>
For us to access the Signup Route we write it in this format http://127.0.0.1:5000/api/signup <br>

Use http://127.0.0.1:5000/api/signup  while Testing your API in insomnia <br/>

Output

![alt text](image-15.png)

<br>
<br>

## Step 4: Create a SignUp API.
When you refer to signup, it typically means the process where users register their details to create an account on a website or application. During the signup process, users provide certain information (e.g., username, email, password) that is stored in the system to uniquely identify them and allow them to access features of the application.

First install pymysql

    pip install pymysql

Then import pymysql like below.

    import pymysql

An endpoint in web development and APIs is a specific URL that allows you to access or interact with the API.
i.e http://127.0.0.1:5000/api/signup    is an endpoint


Update your /api/signup route as follows.
Below is the updated app.py
```python
        from flask import *
        # Create the Flask application instance
        app = Flask(__name__)
        import pymysql

        # Define the sign up Endpoint
        @app.route('/api/signup', methods = ['POST'])
        def signup():
                # Extract values POSTED in the request, store them in varibles 
                username = request.form['username']
                email = request.form['email']
                password = request.form['password']
                phone = request.form['phone']
            
                # COnnect to DB
                connection = pymysql.connect(host='localhost', user='root',
                                                password='',database='BackendAPI')
                # Do the Cursor, initialize the connection
                cursor = connection.cursor()

                # Do SQL Query with 4 placeholders, Confirm table name and columns are as per your DB
                sql = 'insert into users(username,email,password, phone)values(%s,%s,%s,%s)'

                # Prepare data to replace above placeholders
                data = (username, email, password, phone)

                #use Cursor to execute SQL together with the data to replace the 4 placeholders indicated by %s in sql
                cursor.execute(sql, data)
                
                # we need to make a commit to changes to dbase
                connection.commit()

                # Return a message to show a success/data is saved in users table
                return jsonify({"success": "Thank you for Joining"})



        # Run the app if this file is executed directly
        if __name__ == '__main__':
            app.run(debug=True)
``` 

RUn your flask app, The above api can be accessed through  http://127.0.0.1:5000/api/signup   <br>

<b>Explanation </b> <br/>
This code defines a sign-up route (/api/signup) for handling POST requests.<br/>

1. Request handling: It extracts the username, email, password, and phone from the form data submitted in the POST request.<br/>
2. Database connection: It connects to a MySQL database (BackendAPI) using pymysql and creates a cursor to execute the SQL query that inserts user data into the users table.<br/>
3. Commit changes: The transaction is committed to save the data in the database.<br/>
4. Response: It returns a JSON(Key-Value Pairs-Dictionary)response with a success message: "Thank you for Joining".<br/><br/>


Test above api in Insomnia.<br>
NB: In insomnia create a New Folder to store requests (Also rename your requests).
In below requests we use http://127.0.0.1:5000/api/signup as the endpoint, we use POST and the body is exactly as they are defined in our /api/signup Endpoint form request variables.


![alt text](image-24.png)

Confirm the details has been inserted in your Database users table, Practice by inserting 5 records from insomnia and confirm they are saved in users table.

<b>Conclusion</b> <br/>
Above we created a sign-up API accessible via http://127.0.0.1:5000/api/signup endpoint.


## Step 5: Create a Signin API.
Below API endpoint will allow users to Signin using credentials provided in /api/signup in Step 4 above. Update your app.py by adding an /api/signin route as shown below.

# Define the sign in Endpoint

```python
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

```

NB: Above we imported import pymysql.cursors  and used in the cursor cursor = connection.cursor(pymysql.cursors.DictCursor), this will help in returning the user details in a Key Value representation or a Dictionary.

Its important to run and test this endpoint without <b>pymysql.cursors.DictCursor</b> and observe the response is a complete key value pair response. Then include <b>pymysql.cursors.DictCursor</b> include it in cursor and test your endpoint, the result is in form of a Dictionary. <br>

Your complete app.py now looks like below.

```python
        from flask import *

        # Create the Flask application instance
        app = Flask(__name__)
        import pymysql

        # Define the sign up Endpoint
        @app.route('/api/signup', methods = ['POST'])
        def signup():
                email = request.form['email']
                password = request.form['password']
            
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
                email = request.form['email']
                password = request.form['password']  
                
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

```

Test Signin in insomnia.<br/> use http://127.0.0.1:5000/api/signin  as Endpoint <br>
![alt text](image-26.png)

Above screenshot shows when pymysql.cursors.DictCursor is not used, check user details are not in dictionary format - Key Value. Try with pymysql.cursors.DictCursor and observe if the user details has changed to a Dictionary.

<b>Conclusion</b> <br>
In our backend API, we've created a sign-in route accessible via http://127.0.0.1:5000/api/signin endpoint.

## Step 6: Create a Product upload API.
This endpoint will be used by users in uploading their products details.
First create Folder named static in your Flask folder.
Inside static folder create a subfolder named images.(This is where the products photos will be uploaded). <br>Having images placed in a Folder improves space management in the database and make images load faster in your web application.<br><br>
in this route, the image File is saved in static Folder and the image name is saved in the database products details table.<br>

In app.py add below lines to set up Upload directory where our products image will be uploaded <br>
You can place then Just below <b>app = Flask(__name__) </b>

    # setup file upload, os helps in getting the computer file path, later in this code.
    import os
    app.config['UPLOAD_FOLDER'] = 'static/images'


In app.py add below route to create the API Endpoint

```python
    # Define the Add Product Route/Endpoint
    @app.route('/api/add_product', methods=['POST'])
    def add_product():
            # Extract POST Data
            product_name = request.form['product_name']
            product_description = request.form['product_description']
            product_cost = request.form['product_cost']
            # Extract image data
            photo = request.files['product_photo']
            # Get the image file name
            filename = photo.filename
            # Specify computer path where the image will be saved (in static Folder)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # Save your image to that path specified above
            photo.save(photo_path)

            # Connect to DB
            connection = pymysql.connect(host='localhost', user='root',
                                            password='',database='BackendAPI')
            # Create a cursor, initialize connection 
            cursor = connection.cursor()
            # Do Insert SQL, include placeholders 
            sql = 'INSERT INTO product_details (product_name, product_description, product_cost, product_photo) VALUES (%s, %s, %s, %s)'
            # Prepare data to replace placeholders 
            data = (product_name, product_description, product_cost,  filename)
            # using cursor execute sql, providing values in place of placeholders
            cursor.execute(sql, data)

            # Commit the changes to the database
            connection.commit()
            # Return success message in Dictionary Format
            return jsonify({"success": "Product details added successfully"})

```

<b>Test above in insomnia</b>

NB: product_photo must be provided as a File since its an Image.
<br>
use http://127.0.0.1:5000/api/add_product as the endpoint. <br>

![alt text](image-28.png)
<br>
Confirm that the image File has been saved in static/images folder and the rest of product details including the image filename have been saved in the products table. 




## Step 7: Create a Get Products  API.
This endpoint will be used by users to View Posted products,  Here, we will be fetching products details such as product_name, cost, description and product image. <br>
In app.py add below route to create the API Endpoint.

```python
    # Define the Get Product Details Route/Endpoint
    @app.route('/api/get_product_details', methods=['GET'])
    def get_product_details():

        # Connect to the database with DictCursor for direct dictionary results
        connection = pymysql.connect(host='localhost', user='root',
                                            password='',database='BackendAPI')

        # Create a cursor object and fetch all products details from the products_details table
        # pymysql.cursors.DictCursor helps return a Dictionary Format.
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # DO SELECT SQL.
        sql = 'SELECT * FROM product_details'

        # Use cursor to execute SQL
        cursor.execute(sql)

        # Fetch/Get all records into a Dictionary Format
        product_details = cursor.fetchall()


        # Return the products details directly as a dictionay - JSON
        return jsonify(product_details)

```

<b>Test in Insomnia</b> <br/>
In below image shows a Dictionary - JSON Array showing several products displayed
Use http://127.0.0.1:5000/api/get_product_details as the endpoint. <br>
Output
![alt text](image-27.png)


## Step 8: Making an MPESA Payment API.
In the Step we buiil an API Endpoint/Route that will be used to make payment in our E-commerce Web Application. Users can Pay a product via LIPA NA MPESA.
<br>

![alt text](M-PESA-API-Integration.jpg)

M-Pesa Daraja is an API provided by Safaricom, a telecommunications company in Kenya, that allows businesses to integrate M-Pesa's mobile money services into their applications. It enables developers to access a range of M-Pesa functionalities, such as sending and receiving money, checking account balances, and making payments via the M-Pesa platform.
Please check https://developer.safaricom.co.ke/
<br>
After a Suucessful intergration the buyer will get an STK Push like below to complete payment.<br>

<img src="Screenshot_20250220-165048_Phone.jpg" width="400">

<br>

NB: You will need to install requests if not already installed.

    pip install requests

In app.py add below code

```python
    # Mpesa Payment Route 
    import requests
    import datetime
    import base64
    from requests.auth import HTTPBasicAuth

    @app.route('/api/mpesa_payment', methods=['POST'])
    def mpesa_payment():
        if request.method == 'POST':
            # Extract POST Values sent
            amount = request.form['amount']
            phone = request.form['phone']

            # Provide consumer_key and consumer_secret provided by safaricom
            consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
            consumer_secret = "amFbAoUByPV2rM5A"

            # Authenticate Yourself using above credentials to Safaricom Services, and Bearer Token this is used by safaricom for security identification purposes - Your are given Access
            api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
            # Provide your consumer_key and consumer_secret 
            response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
            # Get response as Dictionary
            data = response.json()
            # Retrieve the Provide Token
            # Token allows you to proceed with the transaction
            access_token = "Bearer" + ' ' + data['access_token']

            #  GETTING THE PASSWORD
            timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')  # Current Time
            passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  # Passkey(Safaricom Provided)
            business_short_code = "174379"  # Test Paybile (Safaricom Provided)
            # Combine above 3 Strings to get data variable
            data = business_short_code + passkey + timestamp
            # Encode to Base64
            encoded = base64.b64encode(data.encode())
            password = encoded.decode()

            # BODY OR PAYLOAD
            payload = {
                "BusinessShortCode": "174379",
                "Password":password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": "1",  # use 1 when testing
                "PartyA": phone,  # change to your number
                "PartyB": "174379",
                "PhoneNumber": phone,
                "CallBackURL": "https://coding.co.ke/api/confirm.php",
                "AccountReference": "SokoGarden Online",
                "TransactionDesc": "Payments for Products"
            }

            # POPULAING THE HTTP HEADER, PROVIDE THE TOKEN ISSUED EARLIER
            headers = {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }

            # Specify STK Push  Trigger URL
            url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  
            # Create a POST Request to above url, providing headers, payload 
            # Below triggers an STK Push to the phone number indicated in the payload and the amount.
            response = requests.post(url, json=payload, headers=headers)
            print(response.text) # 
            # Give a Response
            return jsonify({"message": "An MPESA Prompt has been sent to Your Phone, Please Check & Complete Payment"})

```

<b>Test in Insomnia</b> <br/>

Use http://127.0.0.1:5000/api/mpesa_payment as the endpoint. <br>

![alt text](image-29.png)
<br>



## Step 9: Adding CORS - Cross Origin Resource Sharing.
In order to allow this API be accessible by the Front End system to be created.<br>
Frontend and Backend will be two applications to be linked together, By default, web browsers block requests from fronend backend, Hence we need to add CORS in the backend to allow t communicate with Frontend.
<br>
<b>What Does CORS Do?</b> <br>
CORS (Cross-Origin Resource Sharing) is a way for the backend to say, <br>
<i>"Hey, it's okay for frontend to make requests to me!" </i>
<br>
The backend does this by adding special CORS headers in its responses.
We need to enable CORS.<br>
Read more on CORS. <br>
https://blog.postman.com/what-is-cors/ <br><br>

First install CORS in Flask. 

        pip install flask-cors

Then import CORS and Configure in your app
   
        from flask_cors import CORS
        CORS(app)

You can add above code just below  <b>app = Flask(__name__) </b>

In this Github repo, we created an <b>Backend API for E-commerce Web Application</b> <br>
The application provides an API to signup, signin, add_product, get_product_details and MPESA payment integration. This API creates the Back - End of our full-stack application.


## Step 10: Hosting on PythonAnywhere.
Why Host an API on PythonAnywhere?<br>
Imagine you build a Flask API on your computer. It works great, but there's a problem:
💻 It only runs on your computer! No one else can access it. Since its in your computer only - we say its LOCAL.
<br>

<b>Why Use PythonAnywhere?</b> <br>
PythonAnywhere is an onlone platform that: <br>
✅ Keeps your API running 24/7 (Even when your computer/laptop is off).<br>
✅ Allows your API Accessible everywhere/ANytime since Itsts ONLINE <br>
✅ Many users can access the API Backend from the Frontend - (TODO Later). <br>


<b>How it Works:</b><br>
1️⃣ Upload your Flask app from your computer to pythonanywhere . (just like copying files). <br>
2️⃣ Set up a web app (PythonAnywhere runs your app.py). <br>
3️⃣ Your API gets a live URL (https://yourusername.pythonanywhere.com/api/). <br>
4️⃣ Your frontend or mobile app can use it! 🎉 <br>

<b>Example:</b> <br>
Before Hosting - LOCAL: API only runs on http://127.0.0.1:5000/api/ <br>   
After Hosting - ONLINE: API is accessible at https://yourusername.pythonanywhere.com/api/ <br>

<h3>Hosting the API on Pythonanywhere</h3> 
<b>Objective: </b> <br>
<b>By the end of this lesson, students will: </b> <br>
1. Learn how to set up a Flask API on PythonAnywhere.<br>
2. Add CORS support for cross-origin requests. <br>
3. Configure a MySQL database connection. <br>
4. Configure Flask app.py. <br>
5. Configure images location folder - static/images <br>
6. Test the API functionality with insomnia.<br>

<br><br>
<b>Step 10-1: Logging into PythonAnywhere</b> </br>
<b>Access PythonAnywhere:   https://www.pythonanywhere.com  </b> <br>
Sign in with your account or create a new account if you don't have one.<br>

![alt text](image-38.png)

<b>Navigation Menu Overview: </b> <br>
<b>Dashboard:</b> Main page where you manage your account, files, and processes.<br>
<b>Files:</b> Where you can upload, edit, and manage your files.<br>
<b>Consoles: </b>Launch terminals to interact with your Python environment.<br>
<b>Web:</b> Configure your web apps (Flask, Django, etc.) and manage their settings.<br>
<b>Databases:</b> Set up and manage databases for your app (MySQL, SQLite).<br>
<b>Tasks:</b> Schedule tasks to run periodically.<br>

<br>
<b>Step 10-2: Add a New Web Application</b> </br>

![alt text](image-40.png)

Go to the "Web" tab on PythonAnywhere. </br>
Click on Add a New Web Application</br>
Follow the steps : use Latest Python and Flask</br>
Finish creating the Web App. </br>
NB: After creating the Web Application, still under Web Tab check the link where your app will be accessed. Please note it somewhere in a Notepad/Book <br>
     
     https://yourusername.pythonanywhere.com/
<br>
<b>Step 10-3: Install pymysql and flask_cors</b> </br>

![alt text](image-39.png)

Go to the "Consoles" tab on PythonAnywhere. </br>
Start a Bash console.</br>
Install dependencies:</br>
Run the following commands:
   ```
   pip install pymysql
   pip install flask_cors
   ```

<b>Step 10-3: Database Setup</b> </br>
Go to the "Databases" tab on PythonAnywhere. </br>
Create a Pssword. Please Record this password in a Notepab/Book</br>
NB: After password creation, It displays the host and username.  Please Record this details in a Notepab/Book</br>
Open the default database: Please Record this database name in a Notepab/Book</br>
Create the users and product_details tables:</br>

NB: the host, username, password and database names will be needed by app.py during pymysql connections, SO we need to record this details in a Notepad/Book for later use in app.py.

<b>Step 10-4: Flask App Setup</b> </br>
Go to the "Files" tab on PythonAnywhere. </br>
Go to mysite Folder, Open flask_app.py, Copy your API code from your computer and paste it in this File. <br>
Please replace the Database connections with the once created in step 10-3 above.Refer from ypur Notepad/Book. <br>
Replace connections for all routes.<br>
Save this File <br>
while still in mysite Folder, Create a Folder named static/images. This Folder is used for images uploads<br>
Go to "Web" tab on PythonAnywhere. and Reload the application. <br>
Your application is Live at https://yourusername.pythonanywhere.com/ <br>

Your API endpoints can be accessed as:

    https://yourusername.pythonanywhere.com/api/signup
    https://yourusername.pythonanywhere.com/api/signin
    https://yourusername.pythonanywhere.com/api/add_product
    https://yourusername.pythonanywhere.com/api/get_product_details
    https://yourusername.pythonanywhere.com/api/make_payment

Please check your routes spelling, they can be different from above. <br>
































Above API will be accessed in the Front - End (User Side) by React JS and Android Application. <br>

Next is FrontEnd Development using Javascript, React JS.  <br>
Check this link for updates on Frontend Documentation.

<h3>Happy Coding! </h3>






