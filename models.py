from database import get_db_connection

def create_transaction(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO transactions (type, amount, description, date, time)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data.type,
        data.amount,
        data.description,
        data.date,
        data.time
    ))

    conn.commit()
    cursor.close()
    conn.close()
