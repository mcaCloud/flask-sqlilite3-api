# Lo primero que hacemos es obtener la coneccion a la base de DATOS
# Desde nuestro modelo de base de datos importamos la funcion que nos da el return
from models import user_model
from models.db import Database

class User:
    #----------------------------------------
    #----------    INSERT    ----------------
    #----------------------------------------
    # Esta clase obtiene tres parametro para insertar en la DB
    # No le paso el ID porque es autoincremental y lo asigna la base de datos
    def insert_user(name, email,password):
        # Primero me conecto a la base de DATOS
        db = Database.db_connection()

        cursor = db.cursor()
        query = "insert into users(name,email,password) values(?,?,?)"
        cursor.execute(query,[name,email,password])

        db.commit()
        # Esto regresa un true pasa saber que todo fue bien
        return True
    #----------------------------------------
    #----------    DELETE    ----------------
    #----------------------------------------
    def delete_user(id):
        # Primero me conecto a la base de DATOS
        db = db_connection

        cursor = db.cursor()
        query = "delete  users WHERE id=?"
        cursor.excecute(query,[id])

        db.commit()
        # Esto regresa un true pasa saber que todo fue bien
        return True
    #----------------------------------------
    #----------    UPDATE    ----------------
    #----------------------------------------
    # Aqui si le tenemos que pasar todos los parametros incuyendo el ID
    def update_user(id,name,email,password):
        # Primero me conecto a la base de DATOS
        db = db_connection

        cursor = db.cursor()
        query = "update users SET name=?, email=?, password=? WHERE id =?"
        cursor.excecute(query,[id,name,email,password])
        db.commit()
        # Esto regresa un true pasa saber que todo fue bien
        return True

    #----------------------------------------
    #----------    FIND BY ID    -------------
    #----------------------------------------
    # Esta funcion toma un ID y devuelve los campos asociados a ese ID
    def get_by_id(id):
        # Primero me conecto a la base de DATOS
        db = db_connection

        cursor = db.cursor()
        query = "SELECT *  FROM users WHERE id =?"
        cursor.excecute(query,[id])
        db.commit()
        # Aqui lo que necesitamos es que el cursor devuelva un registro porque
        #solo necesitamos un registro por ID. Eso deberia de haber, solo uno
        return cursor.fetchone()

    #----------------------------------------
    #----------    GET_USER    -------------
    #----------------------------------------
    # Esta funcion toma un ID y devuelve los campos asociados a ese ID
    def get_users():
        # Primero me conecto a la base de DATOS
        db = db_connection

        cursor = db.cursor()
        query = "SELECT * FROM users"
        cursor.excecute(query)
        db.commit()
        return cursor.fetchall()
