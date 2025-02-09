import connect
 
def create_reg():

    conn = connect.connection_db()

    cursor = conn.cursor()

    sql_create = "INSERT INTO ClientesFinal (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"
    values=('Alvaro', 'nohaycallealaizquierda', '786543210', 'correo@domini.com', '28_05_2002')

    cursor.execute(sql_create, values)

    conn.commit()

    conn.close()
    cursor.close()