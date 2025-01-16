import psycopg2

def connectio_db():
    conn = psycopg2.connect(
        database="the _bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )
    
    return conn

