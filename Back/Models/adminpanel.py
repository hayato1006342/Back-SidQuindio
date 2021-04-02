from Models import conexion
from datetime import date
from datetime import datetime

class PanelAdmin:
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
        self.datos = 0
        self.search = ''

    def getinfo(self):
        data = {}
        data['info'] = []
        resp = conexion.View('SELECT id,name,type,date FROM places')
        for i in resp:
            data['info'].append({'id':i[0], 'name':i[1] ,"type":i[2],"fecha": format(i[3])})
        return data['info']
    
    def delete(self):
        for i in self.datos:
            respuesta = conexion.Add('delete from places where id = %s',[i])
        return respuesta

    def search_date(self):
        data = {}
        data['admin'] = []
        respuesta = conexion.search("select id,name,type,date from places where name like %s",[self.search])
        for i in respuesta:
            data["admin"].append({'id':i[0],'name':i[1],'type':i[2],'fecha': format(i[3])})
        return data["admin"]
    
    def add_site(self):
        now = datetime.now()
        respuesta = conexion.Add("insert into places (name,type,date,img,imgc1,imgc2,imgc3,category,locate,description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [self.name,self.type,now,self.img,self.imgc1,self.imgc2,self.imgc3,self.category,self.locate,self.description])
        return respuesta
            
