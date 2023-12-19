from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
    UpdateAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from rest_framework.pagination import (
    PageNumberPagination
)

from canales.api.serializers import *
from canales.models import *
     
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
#endpoint que responde a la url api/canales/mensajes
# soporta metodos [GET] y [POST]
class ListCreateMensajeAPIView(ListCreateAPIView):
    serializer_class = MensajeSerializer
    queryset = Mensaje.objects.all().order_by('creado')
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination 
    
#endpoint que responde a la URL /api/chats/<chat_id>/mensajes/
# soporta el metodo [GET]
class ListMensajeAPIView(ListAPIView):
    serializer_class = MensajeSerializer
    queryset = Mensaje.objects.all().order_by('creado')
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        
        chat_id = self.kwargs['chat_id']
        queryset = self.queryset.filter(chat__id=chat_id)
        return queryset
    
#endpoint que responde a la URL /api/chats/<chat_id>/mensajes/<username>/
# soporta el metodo [GET]
class ListMensajeUserAPIView(ListAPIView):
    serializer_class = MensajeSerializer
    queryset = Mensaje.objects.all().order_by('creado')
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        _user= self.kwargs['username']
        queryset = self.queryset
        if _user:
            queryset=queryset.filter(chat__id= chat_id, user__username= _user)
        return queryset
    
