from Models import Conexion

class sites:
    def __init__(self):
        self.name = ''
        self.type = 0
        self.img = ''
        self.imgc1 = ''
        self.imgc2 = ''
        self.imgc3 = ''
        self.prices = 0
        self.category = 0
        self.locate = 0
        self.description = ''

    def get_site(self):
        data = {}
        data['sites'] = []
        rest = Conexion.View("select id,name,img  from places")
        for i in rest:
            data['sites'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['sites']
    
    def add_site(self):
        respuesta = Conexion.Add("insert into places (name,type,date,img,imgc1,imgc2,imgc3,prices,category,locate,description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [self.name,self.type,"2021-03-02",self.img,self.imgc1,self.imgc2,self.imgc3,self.prices,self.category,self.locate,self.description])
        return respuesta