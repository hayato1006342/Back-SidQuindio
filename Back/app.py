from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

from Models.Conexion import *

CORS(app, resources={r"/*": {"origins": "*"}})


from routes.routes import *

app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["register_user"], view_func=user["registro_user_controllers"])
app.add_url_rule(user["recovery_user"], view_func=user["recuperacion_user_controllers"])

app.add_url_rule(user["details_lug"], view_func=user["detalles_user_controllers"])
app.add_url_rule(user["detailss_lug"], view_func=user["detalless_user_controllers"])



app.add_url_rule(user["history_user"], view_func=user["historial_user_controllers"])
app.add_url_rule(user["purchases_user"], view_func=user["purchases_user_controllers"])


app.add_url_rule(admin["create_admin"], view_func=admin["crear_admin_controllers"])
app.add_url_rule(admin["panel_admin"], view_func=admin["panel_admin_controllers"])


app.add_url_rule(places["sites_lug"], view_func=places["atract_lugares_controllers"])
app.add_url_rule(places["hotels_lug"], view_func=places["hoteles_lugares_controllers"])

app.add_url_rule(user["sites_user"], view_func=user["sites_user_controllers"])

if __name__ == '__main__':
    app.run(debug=True,port=5000)