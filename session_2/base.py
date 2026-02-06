import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="/workspaces/semester2-week2/session_2/orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def whole_database(db):

    query = "SELECT * FROM customers;"
    cursor = db.execute(query)

    for part in cursor:
        print(part[2])

def product_categories(db):
    query = """
            SELECT products.category 
            FROM products
            """
    cursor = db.execute(query)
    for part in cursor:
        print(part[0])

def customer_total(db):
    query = """
            SELECT SUM(c.customer_id) 
            FROM customers c
            """
    cursor = db.execute(query)
    for part in cursor:
        print(part[0])

def order_for_customer(db):

    email = input("Enter your email: ")

    query = """
            SELECT c.customer_id 
            FROM customers c 
            WHERE email=?
            """
    cursor1 = db.execute(query, (email,))
    for part1 in cursor1:
        part1 = part1[0]

        query = """
                SELECT o.order_id 
                FROM customers c RIGHT JOIN orders o ON c.customer_id=o.customer_id 
                WHERE o.customer_id=?
                """
        
        print(part1, type(part1))
        
        cursor2 = db.execute(query, (part1,))
        for part2 in cursor2:
            print(f"the email: {email}, has this order: {part2[0]}") 

def product_under_2_pound(db):
    query = """SELECT p.name
            FROM products p
            WHERE p.price < 2"""
    cursor = db.execute(query)
    for part in cursor:
        print(part[0])

def total_spent_per_customer(db):
    query = """
            SELECT SUM(o.total_amount)
            FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id
            GROUP BY o.customer_id
            ORDER BY SUM(o.total_amount) desc LIMIT 5
            """
    cursor = db.execute(query)
    for part in cursor:
        print(part[0])

def orders_per_product_category(db):
    query = """
            SELECT COUNT(o.order_id)
            FROM order_items oi LEFT JOIN  products p ON p.product_id = oi.product_id
            LEFT JOIN orders o ON o.order_id = oi.order_id
            ORDER BY p.category
            """
    cursor = db.execute(query)
    for part in cursor:
        print(part[0])



def main():

    db = get_connection()

    orders_per_product_category(db)

    db.close()


if __name__=="__main__":
    main()
