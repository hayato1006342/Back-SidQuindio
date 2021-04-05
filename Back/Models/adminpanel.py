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
        self.id = 0

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

    def get_prices(self):
        data = {}
        data['admin'] = []
        respuesta = conexion.search("select price,id_place,id from prices where id_place = %s", [self.id])
        if(respuesta):
            for i in respuesta:
                data['admin'].append({'price': i[0],'id_place':i[1], 'id':i[2]})
            return data['admin']
        else:
            return respuesta
    
    def set_price(self):
        respuesta = conexion.Add("insert into prices (id_place, price) values (%s,%s)",[self.id,self.prices])
    
    def delete_price(self):
        respuesta = conexion.Add('delete from prices where id = %s',[self.id])
    
    def bring_data_edit(self):
        data = {}
        data['admin'] = []
        respuesta = conexion.search("select * from places where id = %s",[self.id])
        if(respuesta):
            for i in respuesta:
                data['admin'].append({'id':i[0],'name':i[1],'type':i[2],'date':format(i[3]),'img':i[4],'imgc1':i[5],'imgc2':i[6],'imgc3':i[7],'category':i[8],'locate':i[9],'description':i[10]})
            return data['admin']
        return None
    
    def update(self):
        now = datetime.now()
        respuesta = conexion.Add("update places set name=%s,type=%s,date=%s,img=%s,imgc1=%s,imgc2=%s,imgc3=%s,category=%s,locate=%s,description=%s where id = %s", [self.name,self.type,now,self.img,self.imgc1,self.imgc2,self.imgc3,self.category,self.locate,self.description, self.id])
        return respuesta