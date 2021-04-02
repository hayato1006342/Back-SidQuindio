from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.adminpanel import PanelAdmin

class PanelControllers(MethodView):
    def get(self):
        admin = PanelAdmin()
        respuesta = admin.getinfo()
        return jsonify(respuesta), 200

class RemovePlace(MethodView):
    def post(self):
        content = request.get_json()
        admin = PanelAdmin()
        admin.datos = content
        respuesta = admin.delete()
        return jsonify(respuesta), 200

class SearchPlace(MethodView):
    def post(self):
        content = request.get_json()
        admin = PanelAdmin()
        admin.search = "%" + content.get('search') + "%"
        respuesta = admin.search_date()
        return jsonify(respuesta), 200


class Add_site(MethodView):
    def post(self):
        content = request.get_json()
        admin = PanelAdmin()
        admin.name = content.get("name")
        admin.type = int(content.get("type"))
        admin.img = content.get("img")
        admin.imgc1 = content.get("imgc1")
        admin.imgc2 = content.get("imgc2")
        admin.imgc3 = content.get("imgc3")
        admin.category = int(content.get("category"))
        admin.locate = int(content.get("locate"))
        admin.description = content.get("description")
        respuesta = admin.add_site()
        return jsonify(respuesta),200