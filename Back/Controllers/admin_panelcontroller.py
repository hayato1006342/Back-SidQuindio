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

class GetPrices(MethodView):
    def get(self,id):
        admin = PanelAdmin()
        admin.id = int(id)
        respuesta = admin.get_prices()
        if respuesta:
            return jsonify(respuesta), 200
        else:
            return jsonify(), 400

class SetPrice(MethodView):
    def post(self):
        content = request.get_json()
        admin = PanelAdmin()
        admin.id = content.get('id')
        admin.prices = content.get('price')
        respuesta = admin.set_price()
        return jsonify(), 200

class DeletePrice(MethodView):
    def post(self):
        content = request.get_json()
        admin = PanelAdmin()
        admin.id = int(content)
        respuesta = admin.delete_price()
        return jsonify(), 200

class GetEditPlace(MethodView):
    def get(self,id):
        admin = PanelAdmin()
        admin.id = int(id)
        respuesta = admin.bring_data_edit()
        if(respuesta):
            return jsonify(respuesta), 200
        else:
            jsonify(), 400

class SetEditPlace(MethodView):
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
        admin.id = int(content.get('id'))
        respuesta = admin.update()
        return jsonify(), 200
