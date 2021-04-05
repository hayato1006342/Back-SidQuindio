from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.register import Register
from config import KEY_TOKEN_AUTH
import bcrypt
import jwt
import datetime
import time


class LoginControllers(MethodView):
    def post(self):
        Login = Register()
        content = request.get_json()
        Login.email = content.get("email")
        password = bytes(str(content.get("password")), encoding = 'utf-8')
        respuesta = Login.get_user()
        if respuesta != "":
            password_db = bytes(respuesta[0][4], 'utf-8')
            nombre = respuesta[0][1]
            if bcrypt.checkpw(password, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24), 'email': respuesta[0][2], 'nombre': respuesta[0][1], 'rango': respuesta[0][3]} , KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt), "nombre": respuesta[0][1], "rango": respuesta[0][3]}), 200     
            return jsonify({"Status": "Login incorrecto 22"}), 400
        return jsonify({"Status": "Login incorrecto 11"}), 400
