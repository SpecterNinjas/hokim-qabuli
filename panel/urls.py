from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'panel'

urlpatterns = [

    path('', MainView.as_view(), name="main_page"),
    path('login/', admin_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # MAHALLA
    path("mahalla/", MahallaView.as_view(), name="mahalla"),
    path("mahalla_yaratish/", MahallaCreateView.as_view(), name="mahalla_create"),
    path("mahalla/<int:pk>/", MahallaUpdateView.as_view(), name="mahalla_update"),
    path("mahalla_uchirish/<int:pk>/", MahallaDeleteView.as_view(), name="mahalla_delete"),

    path("mahalla_filter/", ajax_mahalla, name="ajax_mahalla"),

    # MUAMMO TURI
    path("muammo/", MuammoView.as_view(), name="muammo"),
    path("muammo_yaratish/", MuammoCreateView.as_view(), name="muammo_create"),
    path("muammo/<int:pk>/", MuammoUpdateView.as_view(), name="muammo_update"),
    path("muammo_uchirish/<int:pk>/", MuammoDeleteView.as_view(), name="muammo_delete"),

    path("muammo_filter/", ajaxfilter, name="muammo_filter"),

    # CATEGORIYA
    path("kategoriya/", KategoriyaView.as_view(), name="kategoriya"),
    path("kategoriya_yaratish/", KategoriyaCreateView.as_view(), name="kategoriya_create"),
    path("kategoriya/<int:pk>/", KategoriyaUpdateView.as_view(), name="kategoriya_update"),
    path("kategoriya_uchirish/<int:pk>/", KategoriyaDeleteView.as_view(), name="kategoriya_delete"),
    path("ajax/filter_category", ajax_filter_category, name="ajax_filter_category"),

    # Foydalanuvchi
    path("foydalanuvchi/", FoydalanuvchiView.as_view(), name="foydalanuvchi"),
    path("foydalanuvchi/search/", FoydalanuvchiSearchView.as_view(), name="foydalanuvchi_search"),
    path("foydalanuvchi/detail/<int:pk>", FoydalanuvchiDetailView.as_view(), name="foydalanuvchi_detail"),
    path("foydalanuvchi/update/<int:pk>", FoydalanuvchiUpdateView.as_view(), name="foydalanuvchi_update"),

    # HUDUD
    path("hudud/", HududView.as_view(), name="hudud"),
    path("hudud_yaratish/", HududCreateView.as_view(), name="hudud_create"),
    path("hudud/<int:pk>/", HududUpdateView.as_view(), name="hudud_update"),
    path("hudud_uchirish/<int:pk>/", HududDeleteView.as_view(), name="hudud_delete"),

    # MUROJATCHI
    path("murojatchi/", MurojatchiView.as_view(), name="murojatchi"),
    path("murojatchi/search/", MurojatchiSearchView.as_view(), name="murojatchi_search"),
    path("murojatchi/see/<int:pk>", MurojatchiDetailView.as_view(), name="murojatchi_detail"),
    path("murojatchi/<int:pk>/", MurojatchiReplyMessageView.as_view(), name="murojatchi_reply"),
    path("murojatchi_uchirish/<int:pk>/", MurojatchiDeleteView.as_view(), name="murojatchi_delete"),

    # QABUL
    path("qabul/", QabulView.as_view(), name="qabul"),

    # Statistics
    path('statistics/', StatisticsView.as_view(), name='statistics'),

    # ACCEPTED APPLICANTS
    path("accepted/", AcceptedView.as_view(), name="accepted"),
    path("accepted/search/", AcceptedSearchView.as_view(), name="accepted_search"),
    path("accepted/see/<int:pk>", AcceptedDetailView.as_view(), name="accepted_detail"),
    path("accepted/<int:pk>", AcceptedUpdateView.as_view(), name="accepted_update"),

    # Ajax
    path("murojatchi_filter/", murojatchi_filter, name="murojatchi_filter"),

]
