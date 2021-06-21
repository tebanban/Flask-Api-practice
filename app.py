from flask import Flask, jsonify

app = Flask( __name__)

from products import products

@app.route('/hello')
def ping():
    return jsonify ({"message": "Hello from the server!"})

@app.route('/products' )  # by default its using methods=['GET'] 
def getProducts():
    return jsonify ({"products": products, "message": "Products' List"})

@app.route('/products/<string:product_name>' )  # by default its using methods=['GET'] 
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name] # compares url product with list
    print(product_name)
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return "product not found"

if __name__ == '__main__':
    app.run(debug=True, port=4000)

