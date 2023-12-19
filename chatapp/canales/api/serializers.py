from canales.models import Chat, Mensaje
from django.contrib.auth.models import User

from rest_framework import serializers

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        
class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)