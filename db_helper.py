import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ayse659278..",
            database="pandeyji_eatery"
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def insert_order_tracking(order_id, status):
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database")
        return -1
    
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
        cursor.execute(insert_query, (order_id, status))
        connection.commit()
        cursor.close()
        connection.close()
        print("Order tracking inserted successfully!")
        return 1
    except mysql.connector.Error as err:
        print(f"Error inserting order tracking: {err}")
        if connection:
            connection.rollback()
        return -1

def get_order_status(order_id: int):
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database")
        return None
    
    try:
        cursor = connection.cursor()
        query = "SELECT status FROM order_tracking WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result is not None:
            return result[0]
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error getting order status: {err}")
        return None

def insert_order_item(food_item, quantity, order_id):
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database")
        return -1
    
    try:
        cursor = connection.cursor()
        cursor.callproc("insert_order_item", (food_item, quantity, order_id))
        connection.commit()
        cursor.close()
        connection.close()
        print("Order item inserted successfully!")
        return 1
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        if connection:
            connection.rollback()
        return -1

def get_total_order_price(order_id):
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database")
        return None
    
    try:
        cursor = connection.cursor()
        query = f"SELECT get_total_order_price({order_id})"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error getting total order price: {err}")
        return None

def get_next_order_id():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database")
        return None
    
    try:
        cursor = connection.cursor()
        query = "SELECT MAX(order_id) FROM orders"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        if result is None:
            return 1
        else:
            return result + 1
    except mysql.connector.Error as err:
        print(f"Error getting next order ID: {err}")
        return None
