from django.shortcuts import render
from django.views.generic.base import TemplateView



class MaruiLobby (TemplateView):

    template_name = 'lobby.html'
