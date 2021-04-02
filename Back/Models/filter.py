from Models import conexion


class Filters:
    def __init__(self):
        self.search = ''
        self.place = 0
        self.category = 0


    def search_lug(self):
        data = {}
        data['sites'] = []
        rest = conexion.search("select id,name,img  from places where locate = %s and type = 1",[self.place])
        for i in rest:
            data['sites'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['sites']

    def search_category(self):
        data = {}
        data['sites'] = []
        rest = conexion.search("select id,name,img  from places where category = %s and type = 1",[self.category])
        for i in rest:
            data['sites'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['sites']

    def search_data(self):
        data = {}
        data['sites'] = []
        rest = conexion.search("select id,name,img  from places where locate = %s and category = %s and type = 1",[self.place, self.category])
        for i in rest:
            data['sites'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['sites']

    def search_get(self):
        data = {}
        data['sites'] = []
        rest = conexion.search("select id,name,img  from places where name like %s and type = 1",[self.search])
        for i in rest:
            data['sites'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['sites']

#------------------------------hotels

    def search_hotel_get(self):
        data = {}
        data['hotels'] = []
        rest = conexion.search("select id,name,img  from places where name like %s and type = 2",[self.search])
        for i in rest:
            data['hotels'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['hotels']

    def search_data_hotels(self):
        data = {}
        data['hotels'] = []
        rest = conexion.search("select id,name,img  from places where locate = %s and category = %s and type = 2",[self.place, self.category])
        for i in rest:
            data['hotels'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['hotels']
    
    def search_lug_hotel(self):
        data = {}
        data['hotels'] = []
        rest = conexion.search("select id,name,img  from places where locate = %s and type = 2",[self.place])
        for i in rest:
            data['hotels'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['hotels']

    def search_category_hotel(self):
        data = {}
        data['hotels'] = []
        rest = conexion.search("select id,name,img  from places where category = %s and type = 2",[self.category])
        for i in rest:
            data['hotels'].append({'id':i[0],'name':i[1],'img':i[2]})
        return data['hotels']