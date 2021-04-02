from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.details import Details


class DetailControllers(MethodView):
    def get(self,id):
        cmm = Details()
        cmm.id = int(id)
        respuesta= cmm.GetDatail()
        return jsonify(respuesta), 200
