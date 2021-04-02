from flask.views import MethodView
from flask import Flask,jsonify, request
from Models.sites import Sites


#---------- Attractions 

class BringAttractions(MethodView):
    def post(self):
        pass
    
    def get(self):
        attrac = Sites()
        respuesta = attrac.get_site()
        return jsonify(respuesta)

#---------- Hotels

class BringHotel(MethodView):
    def post(self):
        pass

    def get(self):
        hotel = Sites()
        respuesta = hotel.get_hotel_site()
        return jsonify(respuesta)