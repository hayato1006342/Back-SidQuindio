from Models import conexion

class Details:
    def __init__(self):
        self.id = 0

    def GetDatail(self):
        data = {}
        data['sites'] = []
        respuesta = conexion.search("select * from places where id = %s ",[self.id])
        for i in respuesta:
            data['sites'].append({'id':i[0],'name':i[1],'img1':i[4],'img2':i[5],'img3':i[6],'description':i[10]})
        return data['sites']