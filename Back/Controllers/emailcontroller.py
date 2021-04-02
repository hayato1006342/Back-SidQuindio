from flask.views import MethodView
from flask import Flask,jsonify, request
from Send_email.send import enviaremail
from Models.send_email import Send
import random
import bcrypt


class RecoveryEmailControllers(MethodView):
    def post(self):
        e_send = Send()
        e_send.code = random.randint(1000000000000000,9999999999999999)
        content = request.get_json()
        e_send.email = content.get("email")
        check = e_send.send_email()
        if check:
            enviaremail(e_send.email,e_send.code,check)        
            return  jsonify(), 200
        else:
            return jsonify(), 400

class RecoveryPassControllers(MethodView):
    def get(self,id):
        e_pass = Send()
        e_pass.code = int(id)
        check = e_pass.check_code()
        if check:
            if check == 'valid':
                return jsonify({'codestatus':True,'code':e_pass.code}), 200
            else:
                return jsonify({'codestatus':False}), 200
        else:
            return jsonify(), 404


class ModificationPass(MethodView):
    def post(self):
        e_modif = Send()
        content = request.get_json()
        password = content.get('password')
        verifpass = content.get('validatepassword')
        if password == verifpass:
            salt = bcrypt.gensalt()
            e_modif.password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
            e_modif.code = content.get('code')
            check = e_modif.modification_pass()
            if check:
                return jsonify({"modifi":True}),200
            else:
                return jsonify({"modifi":False}),400
        else:
            return jsonify(), 400

