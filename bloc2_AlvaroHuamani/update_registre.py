import connect 

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update ='''
    UPDATE ClientesFinal
    SET Teléfono_Cliente= 000000000
    WHERE id_cliente = 'Roger'
    '''

    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return{"Actualización exitosa"}