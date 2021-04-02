from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

from Models.conexion import *

CORS(app, resources={r"/*": {"origins": "*"}})

from Routes.routes import *

#user
app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["register_user"], view_func=user["registro_user_controllers"])
app.add_url_rule(user["recovery_email_user"], view_func=user["recovery_email_user_controllers"])
app.add_url_rule(user["recovery_pass"], view_func=user["recovery_pass_controllers"])
app.add_url_rule(user["modification_pass"], view_func=user["modification_pass_controllers"])

#authentication

app.add_url_rule(user["authorization_user"], view_func=user["authorization_user_controllers"])

#places
app.add_url_rule(places["attractions_user"], view_func=places["attractions_user_controllers"])
app.add_url_rule(places["hotels_user"], view_func=places["hotels_user_controllers"])
    #-details
app.add_url_rule(places["details_site"], view_func=places["details_site_controllers"])

#filters
    #-attraction
app.add_url_rule(places["filter_attraction"], view_func=places["filter_attraction_controllers"])
app.add_url_rule(places["search_attraction"], view_func=places["search_attraction_controllers"])
    #-hotels
app.add_url_rule(places["filter_hotel"], view_func=places["filter_hotel_controllers"])
app.add_url_rule(places["search_hotel"], view_func=places["search_hotel_controllers"])

#admin
app.add_url_rule(admin["panel_admin"], view_func=admin["panel_admin_controllers"])
app.add_url_rule(admin["panel_remove"], view_func=admin["panel_remove_controllers"])
app.add_url_rule(admin["panel_search"], view_func=admin["panel_search_controllers"])
app.add_url_rule(admin["panel_add_site"], view_func=admin["add_site_controllers"])

if __name__ == '__main__':
    app.run(debug=True,port=5000)