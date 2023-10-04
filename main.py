from flask import Flask,render_template,request,redirect
from dbservice import get_data,insert_product
import psycopg2

conn = psycopg2.connect(
     database="myduka_class", user='postgres', password='T@fari2022')
app = Flask (__name__)


@app.route("/")
def index1():
    return render_template("index.html")

@app.route("/sales", methods =["POST"])
def insert_sales():
     product_id = request.form["product_id"]
     quantity   = request.form["quantity"]
     created_at = request.form["created_at"]

     val = (product_id,quantity,created_at)

     insert_sales(val)

     return redirect("/sales")
     

@app.route("/sales")
def sales():
    get_sales = get_data("sales")
    return render_template("sales.html", mysales = get_sales)

# When inserting a new product, we call the function created in dbservice. And here is where we request 
# the form from products.html at the action and methods attribute and is where the values input by
# user are gotten and pushed to the db table "/products" using the ["POST"] method.
# Pass the values input inside the function in products in the dbservise.py file. 

@app.route("/products", methods=["Post"])
def add_product():
        name           =  request.form["name"]
        buying_price   =  request.form["buying_price"]
        selling_price  =  request.form["selling_price"]
        stock_quantity =  request.form["stock_quantity"]
        values = (name,buying_price,selling_price,stock_quantity)

        insert_product(values)

        return redirect("/products")

@app.route("/products")
def products():
    
    myprods = get_data("products")   
    return render_template("products.html", prd = myprods)

    
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

app.run(debug=True)