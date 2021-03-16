from Models import Conexion
from datetime import date

class paneladmin:
    def __init__(self):
        self.nombre = ''
        self.fecha = ''

    def getinfo(self):
        data = {}
        data['info'] = []
        resp = Conexion.View('SELECT * FROM places')
        print(resp)
        for i in resp:
            data['info'].append({'id':i[0], 'name':i[1] ,"type":i[2],"fecha": format(i[3])})
        return data['info']