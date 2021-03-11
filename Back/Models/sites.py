from Models import Conexion

class sites:
    def __init__(self):
        self.name = ''


    def get_site(self):
        data = {}
        data['sites'] = []
        rest = Conexion.View("select id,name,img  from places")
        for i in rest:
            data['sites'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['sites']