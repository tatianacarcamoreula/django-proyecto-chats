from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Chat(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(verbose_name='title', max_length=60, default ='',)
    
    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades
        como el nombre de la tabla.
        '''
        db_table = 'canales_chat'
        verbose_name = 'chat'
        verbose_name_plural = 'chats'
    def __str__(self):
        return f'{self.id} - {self.nombre}'

class Mensaje(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    user = models.ForeignKey(User, verbose_name= 'user', on_delete=models.CASCADE,)
    chat = models.ForeignKey(Chat, verbose_name= 'chat', on_delete=models.CASCADE,)
    contenido = models.CharField(verbose_name='contenido', max_length=300, default ='',)
    creado =  models.DateTimeField(verbose_name = 'creado', auto_now = True)
    
    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades
        como el nombre de la tabla.
        '''
        db_table = 'canales_mensaje'
        verbose_name = 'mensaje'
        verbose_name_plural = 'mensajes'
        
    def __str__(self):
        return f'{self.id} - {self.user.username} - {self.chat}'