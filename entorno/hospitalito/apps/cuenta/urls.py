from django.urls import path

from apps.cuenta.views import index

name = 'cuenta'
urlpatterns = [
    path('inicio', index, name='index')

]