from Models import conexion
from datetime import timedelta, date, datetime

class Details:
    def __init__(self):
        self.id = 0
        self.email = ''
        self.ticket = ''
        self.amount = 0
        self.price = 0
        self.name = ''

    def GetDatail(self):
        data = {}
        data['sites'] = []
        respuesta = conexion.search("select * from places where id = %s ",[self.id])
        for i in respuesta:
            data['sites'].append({'id':i[0],'name':i[1],'img1':i[4],'img2':i[5],'img3':i[6],'description':i[10]})
        return data['sites']
    
    def GetPrices(self):
        data = {}
        data['prices'] = []
        respuesta = conexion.search("select price from prices where id_place = %s",[self.id])
        for i in respuesta:
            data['prices'].append({'price':i[0]})
        return data['prices']
    
    def Purchase(self):
        now = datetime.now()
        now2 = now + timedelta(days=15)
        respuesta = conexion.Add("insert into record (email,ticket,date_ex,date_com,amount,price,name_place) values (%s,%s,%s,%s,%s,%s,%s)",[self.email,self.ticket,now2,now,self.amount,self.price,self.name])

    def GetPurchaseHistory(self):
        data = {}
        data['history'] = []
        respuesta = conexion.search("select ticket, date_ex, date_com, amount, price, name_place from record where email = %s",[self.email])
        if(respuesta):
            for i in respuesta:
                data['history'].append({'ticket':i[0], 'date_ex': i[1], 'date_com':i[2], 'amount':i[3], 'price': i[4], 'name_place': i[5]})
            return data['history']
        else:
            return None