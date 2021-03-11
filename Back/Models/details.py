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
            data['sites'].append({'id':i[0],'name':i[1],'img1':i[3],'img2':i[4],'img3':i[5],'price':i[6],'description':i[9]})
        return data['sites']