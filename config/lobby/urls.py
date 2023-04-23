from django.urls import path
from . import views

app_name = 'lobby'
urlpatterns = [
    path('', views.MaruiLobby.as_view(), name='index'),
]