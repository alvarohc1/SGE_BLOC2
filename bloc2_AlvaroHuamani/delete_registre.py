import connect

def delete_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_delete ='''
    DELETE FROM ClientesFinal
    WHERE id_cliente = 'Alvaro'
    '''
    cursor.execute(sql_delete)
    conn.commit()

    cursor.close()
    conn.close()

    return{"Borrado exitoso"}