from Controllers.controllers import LoginUserControllers, RegistroUserControllers, RecuperacionUserControllers, DetallesUserControllers, Add_site , PanelAdminControllers, HistorialUserControllers, AtractivosLugaresControllers, HotelesLugaresControllers, PurchasesUserControllers, BringData, DetallesUsersControllers

user = {
    "login_user": "/api/v01/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "register_user": "/api/v01/registro", "registro_user_controllers": RegistroUserControllers.as_view("register_api"),
    "recovery_user": "/api/v01/recuperacion", "recuperacion_user_controllers": RecuperacionUserControllers.as_view("recodery_api"),
    "details_lug":"/api/v01/detalles","detalles_user_controllers": DetallesUserControllers.as_view("details_api"),
    "detailss_lug":"/api/v01/detalless/<id>","detalless_user_controllers": DetallesUsersControllers.as_view("detailss_api"),
    "history_user":"/api/v01/historial","historial_user_controllers": HistorialUserControllers.as_view("history_api"),
    "purchases_user":"/api/v01/compras","purchases_user_controllers": PurchasesUserControllers.as_view("purchases_api"),
    "sites_user":"/api/v01/sites","sites_user_controllers": BringData.as_view("sites_api")
}


admin = {
	"create_admin":"/api/v01/crear","crear_admin_controllers": Add_site.as_view("create_api"),
	"panel_admin":"/api/v01/panel","panel_admin_controllers": PanelAdminControllers.as_view("panel_api")
}

places = {
	"sites_lug":"/api/v01/atractivos","atract_lugares_controllers": AtractivosLugaresControllers.as_view("Contenido_api"),
	"hotels_lug":"/api/v01/hoteles","hoteles_lugares_controllers": HotelesLugaresControllers.as_view("Hotels_api")
}