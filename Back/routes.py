from controllers import LoginUserControllers, RegistroUserControllers, RecuperacionUserControllers, DetallesUserControllers, CrearAdminControllers, PanelAdminControllers, HistorialUserControllers, AtractivosLugaresControllers, HotelesLugaresControllers

user = {
    "login_user": "/api/v01/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "register_user": "/api/v01/registro", "registro_user_controllers": RegistroUserControllers.as_view("register_api"),
    "recovery_user": "/api/v01/recuperacion", "recuperacion_user_controllers": RecuperacionUserControllers.as_view("recodery_api"),
    "details_lug":"/api/v01/detalles","detalles_user_controllers": DetallesUserControllers.as_view("details_api"),
    "history_user":"/api/v01/historial","historial_user_controllers": HistorialUserControllers.as_view("history_api")
}


admin = {
	"create_admin":"/api/v01/crear","crear_admin_controllers": CrearAdminControllers.as_view("create_api"),
	"panel_admin":"/api/v01/panel","panel_admin_controllers": PanelAdminControllers.as_view("panel_api")
}

places = {
	"sites_lug":"/api/v01/atractivos","atract_lugares_controllers": AtractivosLugaresControllers.as_view("Contenido_api"),
	"hotels_lug":"/api/v01/hoteles","hoteles_lugares_controllers": HotelesLugaresControllers.as_view("Hotels_api")
}