from Models import conexion
from datetime import timedelta, date, datetime

class Send:
    def __init__(self):
        self.email = ''
        self.password = ''
        self.code = 0

    def send_email(self):
        respuesta = conexion.search('select name,email from users where email = %s',[self.email])
        if respuesta:
            for i in respuesta:
                now = datetime.now() + timedelta(hours=24)
                resp = conexion.Add('update users set code=%s, recovery_date= %s where email = %s',[self.code,now,self.email])
                return i[0]
        else:
            return None
    
    def check_code(self):
        respuesta = conexion.search('select code, recovery_date from users where code = %s',[self.code])
        if respuesta:
            for i in respuesta:
                now = datetime.now()
                if now.strftime('%Y %m %d %H %M %S') > i[1].strftime('%Y %m %d %H %M %S'):
                    return 'invalid'
                else:
                    return 'valid'
        else: 
            return None
    
    def modification_pass(self):
        now = datetime.now()
        respuesta = conexion.Add('update users set indentify = %s, recovery_date = %s where code = %s',[self.password,now,self.code])
        if respuesta:
            return 'Ok'

