
from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        return jsonify({"Ingreso Exitoso": True}), 200


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

        return jsonify({"Registro Exitoso": True}), 200
    
    def get():
        pass
    
    def put():
        pass
     
class DetallesUserControllers(MethodView):
    def post(self):
        time.sleep(3)
        return jsonify({"Compra Realizada": True}), 200

class HistorialUserControllers(MethodView):
    def get(self):
        time.sleep(3)
        datos = "ASQ"
        return jsonify({"datos": datos }), 200


class CrearAdminControllers(MethodView):
    def post(self):
        time.sleep(3)
        return jsonify({"Creado con exito": True}), 200

class PanelAdminControllers(MethodView):
    def get(self):
        time.sleep(3)
        datos = "ASQ"
        return jsonify({"datos": datos }), 200

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

