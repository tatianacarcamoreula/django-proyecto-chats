from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication

from canales.models import *
from canales.api.serializers import *

#endpoint que responde a la url /api/canales/chats/<pk>
# permite las acciones [GET], [PUT] y [POST]
class ListCreatePutChat(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = ChatSerializer
    http_method_names = ('get', 'post', 'put', 'patch',)
    queryset = serializer_class.Meta.model.objects.all().order_by('id')
    def get_queryset(self):
        chat_id = self.request.query_params.get('pk')
        queryset = self.queryset
        if chat_id:
            queryset=queryset.filter(chat__id= chat_id)
        return queryset