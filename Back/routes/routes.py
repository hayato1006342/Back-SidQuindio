from Controllers.getsitescontroller import BringAttractions, BringHotel
from Controllers.logincontroller import LoginControllers
from Controllers.registercontroller import RegisterControllers
from Controllers.authenticationcontroller import AuthorizationControllers
from Controllers.getfiltersitecontroller import FilterAttractionControllers, SearchAttractionControllers, FilterHotelControllers, SearchHotelControllers
from Controllers.detailcontroller import DetailControllers
from Controllers.admin_panelcontroller import PanelControllers, RemovePlace, SearchPlace, Add_site
from Controllers.emailcontroller import RecoveryEmailControllers, RecoveryPassControllers, ModificationPass

user = {
    "login_user": "/api/v01/login", "login_user_controllers": LoginControllers.as_view("login_api"),
    "register_user": "/api/v01/registro", "registro_user_controllers": RegisterControllers.as_view("register_api"),
    "authorization_user": "/api/v01/authorization", "authorization_user_controllers": AuthorizationControllers.as_view("authentication_api"),
    "recovery_email_user": "/api/v01/recovery", "recovery_email_user_controllers": RecoveryEmailControllers.as_view("recovery_api"),
    "recovery_pass": "/api/v01/recovery-passw/<id>", "recovery_pass_controllers": RecoveryPassControllers.as_view("recovery_pass_api"),
    "modification_pass": "/api/v01/modification-pass", "modification_pass_controllers": ModificationPass.as_view("Modification_pass_api"),
}

places = {
    "attractions_user":"/api/v01/attractions","attractions_user_controllers": BringAttractions.as_view("sites_api"),
    "hotels_user":"/api/v01/hotels","hotels_user_controllers": BringHotel.as_view("hotels_api"),
    "filter_attraction":"/api/v01/filter/attraction", "filter_attraction_controllers" : FilterAttractionControllers.as_view("filter_attraction_api"),
    "search_attraction":"/api/v01/search/attraction", "search_attraction_controllers" : SearchAttractionControllers.as_view("search_attraction_api"),
    "filter_hotel":"/api/v01/filter/hotel", "filter_hotel_controllers" : FilterHotelControllers.as_view("filter_hotel_api"),
    "search_hotel":"/api/v01/search/hotel", "search_hotel_controllers" : SearchHotelControllers.as_view("search_hotel_api"),
    "details_site":"/api/v01/details/<id>","details_site_controllers": DetailControllers.as_view("details_api"),
}

admin = {
    "panel_admin":"/api/v01/panel","panel_admin_controllers": PanelControllers.as_view("panel_api"),
    "panel_remove":"/api/v01/remove","panel_remove_controllers": RemovePlace.as_view("remove_api"),
    "panel_search":"/api/v01/admin/search","panel_search_controllers": SearchPlace.as_view("panel_search_api"),
    "panel_add_site":"/api/v01/admin/add","add_site_controllers": Add_site.as_view("add_site_api"),
}
