import connect 

def alter_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_alter ='''
    ALTER TABLE ClientesFinal
    RENAME COLUMN Nombre_Cliente TO
    id_cliente;
    '''

    cursor.execute(sql_alter)
    conn.commit()

    cursor.close()
    conn.close()

    return{"Alteración exitosa"}

#Este función es para agregar una columna id para el registro