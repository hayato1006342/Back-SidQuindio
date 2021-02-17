from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["register_user"], view_func=user["registro_user_controllers"])
app.add_url_rule(user["recovery_user"], view_func=user["recuperacion_user_controllers"])
app.add_url_rule(user["details_lug"], view_func=user["detalles_user_controllers"])
app.add_url_rule(user["history_user"], view_func=user["historial_user_controllers"])


app.add_url_rule(admin["create_admin"], view_func=admin["crear_admin_controllers"])
app.add_url_rule(admin["panel_admin"], view_func=admin["panel_admin_controllers"])


app.add_url_rule(places["sites_lug"], view_func=places["atract_lugares_controllers"])
app.add_url_rule(places["hotels_lug"], view_func=places["hoteles_lugares_controllers"])


