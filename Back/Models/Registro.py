from Models import Conexion
class Registro:
    def __init__(self):
        self.name = ''
        self.email = ''
        self.password = ''

    
    def create_user(self):
        respuesta = Conexion.Add("insert into users (name,email,range_user,indentify) values(%s,%s,1,%s)",[self.name,self.email,self.password])


    def get_user(self):
        data = {}
        data['Login'] = []
        respuesta = Conexion.search("select * from users where email = %s ",[self.email])
        return respuesta