import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",   # 🔥 NOT localhost, NOT env
        user="root",
        password="sky5",
        database="shop_record_db",
        port=3306
    )
