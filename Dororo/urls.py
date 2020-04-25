from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include(('gestion.urls','gestion'), namespace='gestion')),
    path('admin/',admin.site.urls),
]
