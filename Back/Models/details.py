from Models import Conexion
class details:
    def __init__(self):
        self.id = 0

    def GetDatail(self):
        data = {}
        data['sites'] = []
        respuesta = Conexion.search("select * from places where id = %s ",[self.id])
        print(respuesta)
        for i in respuesta:
            data['sites'].append({'id':i[0],'name':i[1],'img1':i[4],'img2':i[5],'img3':i[6],'price':i[6],'description':i[11]})
        return data['sites']