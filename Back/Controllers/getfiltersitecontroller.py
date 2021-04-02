from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.filter import Filters


# --------------------- filter attractions
class FilterAttractionControllers(MethodView):
    def post(self):
        content = request.get_json()
        attrac = Filters()
        attrac.place = int(content.get("place"))
        attrac.category = int(content.get("category"))

        if attrac.place and attrac.category != 0:
            resultado = attrac.search_data()
        else:
            if attrac.place != 0:
                resultado = attrac.search_lug()
            if attrac.category != 0 :
                resultado = attrac.search_category()
        return jsonify(resultado),200


class SearchAttractionControllers(MethodView):
    def post(self):
        content = request.get_json()
        attrac = Filters()
        attrac.search = "%" + content.get('search') + "%"
        respuesta = attrac.search_get()
        return jsonify(respuesta),200

# --------------------- filter Hotels

class FilterHotelControllers(MethodView):
    def post(self):
        content = request.get_json()
        hotel = Filters()
        hotel.place = int(content.get("place"))
        hotel.category = int(content.get("category"))
        if hotel.place and hotel.category != 0:
            resultado = hotel.search_data_hotels()
        else:
            if hotel.place != 0:
                resultado = hotel.search_lug_hotel()
            if hotel.category != 0 :
                resultado = hotel.search_category_hotel()
        return jsonify(resultado), 200

class SearchHotelControllers(MethodView):
    def post(self):
        content = request.get_json()
        hotel = Filters()
        hotel.search = "%" + content.get('search') + "%"
        respuesta = hotel.search_hotel_get()
        return jsonify(respuesta),200
