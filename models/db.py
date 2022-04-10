                    #---------------------#
                    # CONTROL DE ERRORES  #
                    #---------------------#
# Utilizo al módulo de excepcciones para controlar los errores a la hora de importar
try:
    # Importo el módulo de sqlite3
    import sqlite3
    # Para saber que tipo de error en la interaccion con la base de datos
    from sqlite3 import Error
# Pongo un mensaje propio para controlar mejor las excepciones
except ModuleNotFoundError as err:
    msg('Oppssss...Parece que algo va mal con un módulo', err)
                    #---------------------#
                    #   CLASE SQLLITE3    #
                    #---------------------#
# Creo un a clase con todos los metodos necesarios para realizar consultas con la base de datos
class Database:
    #----------------------------------------
    #----------    CONEXION BD    -----------
    #----------------------------------------
    def db_connection():
        # La variable de conexión la pruebo dentro de un try ara controlar errores
        try:
             # ----- CREAR DB -----------
             # Creo un objeto de conección
             ## Esto me crea un archivo .db en el directorio actual del módulo
             con = sqlite3.connect('myapp.db')
             # Regreso la conexión para utilizarla desde el main
             return con
        # Utilizo la fuincion de Sqllite3 ERROR que la importamos más arriba
        # Es lo mismo que utilizar Exception as ...
        except Exception as e:
             # Imprimo el error de SQLLITE
             print('Hay un error de conexión', e)
    #----------------------------------------
    #----------    CREATE    ----------------
    #----------------------------------------
    def create_table():
        #-----------------------------------
        # --------------TABLA -------------
        sql = """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name Text NOT NULL,
                    email varchar NOT NULL,
                    password varchar NOT NULL
                )
        """
        # Establecemos la conección a la base de datos
        db = Database.db_connection()
        # Una vez que tengamos la conexion hacemos un excecute
        # Le paso como parametro la variable SQL con la consulta
        db.execute(sql)
        #-----------------------------------
        # --------- GUARDAR en DB  ---------
        # Esto lo que hace es guardarme los cambios en la base de datos
        db.commit()
