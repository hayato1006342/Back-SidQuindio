"""from flask.views import MethodView
from flask import jsonify, request
from Models.users import users
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
import time



class LoginUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = bytes(str(content.get("password")), encoding = 'utf-8')
        if users.get(email):
            password_db = users[email]["password"]
            nombre = users[email]["nombre"]
            if bcrypt.checkpw(password, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10), 'email': email, 'nombre': nombre}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt), "nombre": nombre}), 200     
            return jsonify({"Status": "Login incorrecto 22"}), 400   
        return jsonify({"Status": "Login incorrecto 11"}), 400



class RecuperacionUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        content = request.get_json()
        codigo = content.get("codigo")
        password = content.get("password")
        password = content.get("validatepassword")
        return jsonify({"": True}), 200
        


class RegistroUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        content = request.get_json()
        nombre = content.get("nombre")
        email = content.get("email")
        password = content.get("password")
        validatepassword = content.get("validatepassword")

        if password == validatepassword:
            salt = bcrypt.gensalt()
            hash_password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)

            users[email] = {"password": hash_password, "email": email, "nombre": nombre}
            print(users[email])
            return jsonify({"Status": "Registro ok",
                            "password_encriptado": str(hash_password),
                            "password_plano": str(password)}), 200



        return jsonify({"Registro Exitoso": True}), 200
    
    def get():
        pass
    
    def put():
        pass
     
class DetallesUserControllers(MethodView):
    def post(self):
    	time.sleep(3)
    	return jsonify({"Status": "No ha enviado un token"}), 200

    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"), "nombre": data.get("nombre")}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403


class HistorialUserControllers(MethodView):
    def get(self):
       time.sleep(3)
       datos = "ASQ"
       return jsonify({"datos": datos }), 200

    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email")}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403




class CrearAdminControllers(MethodView):
    def post(self):
        time.sleep(3)
        return jsonify({"Creado con exito": True}), 200

    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email")}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403

class PanelAdminControllers(MethodView):
    def get(self):
        time.sleep(3)
        datos = "ASQ"
        return jsonify({"datos": datos }), 200

    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email")}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403

class AtractivosLugaresControllers(MethodView):
    def get(self):
        time.sleep(3)
        datos = "ASQ"
        return jsonify({"datos": datos }), 200

class HotelesLugaresControllers(MethodView):
    def get(self):
        time.sleep(3)
        datos = "ASQ"
        return jsonify({"datos": datos }), 200


class PurchasesUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        content = request.get_json()
        site = content.get("site")
        locate = content.get("locate")
        ticket = content.get("ticket")
        amount = content.get("amount")
        value = content.get("value")
        expiration = content.get("expiration")
        return jsonify({"Mensaje": "Compra realizada" }), 200

"""