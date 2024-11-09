from app.conexion import ConexionBD

def create(titulo, descripcion, fecha_creacion, fecha_vencimiento):
    conexion = ConexionBD()
    conn = conexion.conectar()
    cursor = conn.cursor()
    mysql_query = "INSERT INTO tareas (titulo, descripcion, fecha_creacion, fecha_vencimiento) VALUES (%s, %s, %s, %s)"
    values = (titulo, descripcion, fecha_creacion, fecha_vencimiento)
    cursor.execute(mysql_query, values)
    conn.commit()
    cursor.close()
    print("Tarea creada")

def delete(id):
    conexion = ConexionBD()
    conn = conexion.conectar()
    cursor = conn.cursor()
    mysql_query = "DELETE FROM tareas WHERE id = %s"
    values = (id,)
    cursor.execute(mysql_query, values)
    conn.commit()
    cursor.close()

def read():
    conexion = ConexionBD()
    conn = conexion.conectar()
    cursor = conn.cursor()
    mysql_query = "SELECT * FROM tareas"
    cursor.execute(mysql_query)
    results = cursor.fetchall()
    cursor.close()
    return results

def update(titulo, descripcion, fecha_inicio, fecha_finalizacion, id):
    conexion = ConexionBD()
    conn = conexion.conectar()
    cursor = conn.cursor()
    mysql_query = "UPDATE tareas SET titulo = %s, descripcion = %s, fecha_creacion = %s, fecha_vencimiento = %s WHERE id = %s"
    values = (titulo, descripcion, fecha_inicio, fecha_finalizacion, id)
    cursor.execute(mysql_query, values)
    conn.commit()
    cursor.close()

def get_task_by_id(task_id):
    conexion = ConexionBD()
    conn = conexion.conectar()
    cursor = conn.cursor()
    mysql_query ="SELECT * FROM tareas WHERE id = %s"
    values = (task_id,)
    cursor.execute(mysql_query,values )
    task = cursor.fetchone()
    cursor.close()
    return task


if __name__ == "__main__":
    pass