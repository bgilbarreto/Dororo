from django.contrib import admin
from django.urls import include, path
from gestion.views import Home, Hist, Pelea, items, insertBattle, insertObject
from django.contrib.auth import views as auth_views
from gestion.views import demon_print

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',auth_views.LoginView.as_view(template_name = "login.html"), name = "login"),
    path('logout/',auth_views.LogoutView.as_view(template_name = "login.html"), name = "logout"),
    path('historial/',Hist.as_view(), name= 'historial'),
    path('pelea/',Pelea.as_view(), name = 'pelea'),
    path('objetos/',items.as_view(), name = 'objetos'),
    path('agegarPelea/',insertBattle.as_view(), name='inBattle'),
    path('agregarObjeto/', insertObject.as_view(), name='inObj'),
    path('demon/print',demon_print,name='demon_print_one')
]