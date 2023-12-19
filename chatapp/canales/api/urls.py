from django.contrib import admin
from django.urls import path, include

from canales.api.views import *
urlpatterns = [
    path('canales/mensajes/', ListCreateMensajeAPIView.as_view()),
    path('chats/<int:chat_id>/mensajes/', ListMensajeAPIView.as_view()),
    path('chats/<int:chat_id>/mensajes/<str:username>/', ListMensajeUserAPIView.as_view()),
    path('canales/', include('canales.api.routers')),
]
#:pk>/<int