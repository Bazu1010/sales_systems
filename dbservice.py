import psycopg2
from flask import request, redirect

conn = psycopg2.connect(
     database="myduka_class", user='postgres', password='T@fari2022')


# Getting Data
def get_data(table_name):
    cursor = conn.cursor()
    t= f"select * from {table_name}"
    cursor.execute(t)
    all_data = cursor.fetchall()
    return all_data

## Inserting a new product in the table
def insert_product(values):
    cursor = conn.cursor()
    insert_products="INSERT INTO products(name,buying_price,selling_price,stock_quantity) VALUES(%s,%s,%s,%s)"
    cursor.execute(insert_products,values)
    conn.commit()

    

# Inserting Sale

def insert_sale(values):
    cursor = conn.cursor()
    insert_s = "INSERT INTO sales(product_id,quantity,created_at) VALUES(%s,%s,%s)"
    cursor.execute(insert_s,values)
    conn.commit()
   


  