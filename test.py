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
