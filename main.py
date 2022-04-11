# Importo la libreria para trabajar con objetos json
# Con jsonify podemos pasar de un diccionario a un objeto json
# Las APIs generalmente trabajan con objetos json
# COn request me permite hacer los POST-GET
from flask import Flask, jsonify, redirect, url_for, render_template
from flask import request
from flask import session

# Esto lo importo para interactuar con la base de datos y sus metodos
# Menciono el directorio, el fichero y la clase dentro del fichero
from models.user_model import User
from  models.db import Database
from models.new_user import Model_new_user
from models.validation import Validation
#-------------------------------
#       APLICACION
#-------------------------------
# Creo una instancia de Flask
# Esto es importante porque a traves de esto la aplicacion
# sabe donde buscar los archivos :html,statiics ,ect
# Necesita saber si la plaicacion va a ser ejecutada desde el archivo pricipal o desde otro archivo
app = Flask(__name__)

# his session has a default time limit of some number of minutes or hours or days after which it will expire
app.config["SESSION_PERMANENT"] = False
# It will store in the hard drive
#  it is an alternative to using a Database or something else like that.
app.config["SESSION_TYPE"] = "filesystem"

app.secret_key = 'ItShouldBeAnythingButSecret'

                #-------------------------------
                #       CREAR RUTAS
                #-------------------------------
#---------------
#    INDEX
#----------------
# Esto es un decorador que me ayudar a genera rutas
# Lo utiliza Flask para saber a que  URL acceder
# Paso como argumento la ruta de la URL en este caso Root
# Esta ruta lleva ligada una funcionindex
@app.route('/')
# Ahora defino una funcion home que esta envuelta en el decorador app.route
# Aqui se define lo que hay que ejecutar si el ‘endpoint’ de la URL
#definida es solicitado por un usuario. Su valor de retorno determina lo que el
#usuario verá cuando cargue la página
def index():
    return render_template('index.html')

#---------------
#    LOGIN
#----------------
# Necesito grabar cuando el usuario evía el formulario
@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        # Obtengo la variables que me llegan por POST
        # Aún no puedo utilizar el jsonfy bien :P
        email = request.form['email']
        password = request.form['password']
        # Utilizo mi modelo de new user y le paso por parametro mis variables
        user = Validation.login(email, password)
        #------------------
        #    VALIDATION
        #------------------
        # Comparo las variables que me llegan del form con la info de la BD
        # Si la información existe dentro del fetchone que obtuve de la base de DATOS
        # Entonces significa que si existe ese usuario
        if email in user and password in user:
            # Obtengo el nombre de la persona para usarlo con id de session
            id_session = user[1]
            # Asigno la variable al id de session
            session['user'] = id_session
            # Si el usuario existe lo redirijo a la página dashboard
            # Invboco al metodo dashboard y le paso el ID de session actual para validarlo
            return redirect('/dashboard')
    else:
        return "<h1>Ha ocurrido un error de authenticación.</h1>"    #if the username or password does not matches

#---------------
#    LOGOUT
#----------------
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user', None)
   return redirect('/')

#---------------
#    REGISTER
#----------------
# Necesitamos saber de donde vienen los datos
# Utilizamos el GET POST para obtener los datos del usuario
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #---- EXTRAIGO LA INFO------
        # Variable para almacenar la info del formulario
        #user_details = request.get_json()
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #-------------------
        #    OBJETO USUARIO
        #-------------------
        # Aqui creo un objeto de Usuario
        # Le paso por parámetro los datos del formulario
        user = Model_new_user(name,email,password)
        # Obtengo los atributo del objeto y los paso como parametro
        # Esto es para realizar la consulta en la BD
        #------------------------
        #    INSERTO DATOS EN BD
        #------------------------
        User.insert_user(user.name,user.email,user.password)

        return redirect('/')
    else:
        #return jsonify(object_user)
        return redirect('/')

#---------------
#    DASHBOARD
#----------------
@app.route('/dashboard')
# Recibo como parámetro el id_session
def dashboard():
    # Si es igual al session ID grabado en el sistema...
    if session['user']:
        return render_template('home.html')


    return '<h1>You are not logged in.</h1>'


@app.route('/users', methods = ['GET'])
def show_users():
    users = User.get_users()
    return jsonify(users)

# Esto es para saber si el script se ejecuta directo desde aqui y no
# Esta siendo importado
if __name__ == "__main__":

    Database.create_table()
    # Aqui activo el debuger en la aplicacion para poder ver los cambios en vivo cuando los hago
    # Esto es produccion ya no es recomendable
    # Aqui le indico el puerto 8080
    app.run(host="127.0.0.1",port=8080, debug=True)
