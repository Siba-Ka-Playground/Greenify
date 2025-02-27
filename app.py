from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # My MySQL username
        password="Shiba@21",  # My MySQL password
        database="product_list" #My Database Name
    )

# Route to load the main page
@app.route('/')
def index():
    # Fetch products from the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product_vs_alternative")
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

# Route to get product alternatives via AJAX
@app.route('/get_alternatives/<Product>')
def get_alternatives(Product):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Alternative FROM product_vs_alternative WHERE Product = %s", (Product,))
    alternatives = cursor.fetchall()
    conn.close()
    return jsonify(alternatives)

if __name__ == '__main__':
    app.run(debug=True)
