from models import user_model
from models.db import Database

class Validation:
        #----------------------------------------
        #----------    RETRIVE USER    -------------
        #----------------------------------------
        # Esta funcion toma un ID y devuelve los campos asociados a ese ID
        def login(email,password):
            var1 = str(email)
            var2 = password
            # Primero me conecto a la base de DATOS
            db = Database.db_connection()
            # Ahora creo el cursor
            cursor = db.cursor()
            # Realizo la consulta a la base de datos
            query = "SELECT * FROM users WHERE email = ? AND password = ?"

            try:
                # Ejecuto la consulta
                cursor.execute(query, [var1,var2])
            except Exception as e:
                return(e)
            else:
                # Como solo puede haber un resultado hago un fetch obtener# Lo regreso para trabajar con ese usuario
                return cursor.fetchone()
