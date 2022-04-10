# Esto es un modelo de la clase profesor
class Model_new_user:

    # Este va a ser nuestro constructor con las variables que recibimos como parametro
    def __init__(self,name, email, password):

        self.name = name
        self.email = email
        self.password = password

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getEmail(self):
        return self.email

    def setEmail(self,email):
        self.email = email

    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password = passwword
