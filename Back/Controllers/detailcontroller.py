from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.details import Details



class DetailControllers(MethodView):
    def get(self,id):
        cmm = Details()
        cmm.id = int(id)
        respuesta= cmm.GetDatail()
        return jsonify(respuesta), 200

class BringPricesControllers(MethodView):
    def get(self,id):
        cmm = Details()
        cmm.id = int(id)
        respuesta = cmm.GetPrices()
        return jsonify(respuesta), 200

class FinalizePurchase(MethodView):
    def post(self):
        cmm = Details()
        content = request.get_json()
        cmm.email = content.get('user')
        cmm.name = content.get('name')
        cmm.ticket = content.get('code')
        cmm.amount = int(content.get('amount'))
        cmm.price = float(content.get('value'))
        respuesta = cmm.Purchase()
        return jsonify(), 200

class PurchaseHistory(MethodView):
    def post(self):
        cmm = Details()
        content = request.get_json()
        cmm.email = content.get('user')
        respuesta = cmm.GetPurchaseHistory()
        if(respuesta):
            return jsonify(respuesta), 200
        return jsonify(), 400
