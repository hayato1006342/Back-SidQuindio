from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.register import Register
import bcrypt

class RegisterControllers(MethodView):
    def post(self):
        content = request.get_json()
        name = content.get("nombre")
        email = content.get("email")
        password = content.get("password")
        validatepassword = content.get("validatepassword")
        register = Register()
        if password == validatepassword:
            salt = bcrypt.gensalt()
            register.password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
            register.name = name
            register.email = email
            respuesta = register.create_user()
            return jsonify({"Status": "Registro ok",
                            "password_encriptado": str(register.password),
                            "password_plano": str(password)}), 200

        return jsonify({"Registro Exitoso": True}), 200
    
    def get():
        pass
    
    def put():
        pass