from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["registro_user"], view_func=user["registro_user_controllers"])
app.add_url_rule(user["recuperacion_user"], view_func=user["recuperacion_user_controllers"])
app.add_url_rule(user["detalles_lug"], view_func=user["detalles_user_controllers"])
app.add_url_rule(user["historial_user"], view_func=user["historial_user_controllers"])


app.add_url_rule(admin["crear_admin"], view_func=admin["crear_admin_controllers"])
app.add_url_rule(admin["panel_admin"], view_func=admin["panel_admin_controllers"])


app.add_url_rule(lugares["atractivos_lug"], view_func=lugares["atract_lugares_controllers"])
app.add_url_rule(lugares["hoteles_lug"], view_func=lugares["hoteles_lugares_controllers"])




