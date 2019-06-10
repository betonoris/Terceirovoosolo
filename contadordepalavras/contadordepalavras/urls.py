from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paginainicial, name='inicio'),
    path('contar/', views.contar, name='contar'),
    path('notas/', views.notas, name='notas'),
]


