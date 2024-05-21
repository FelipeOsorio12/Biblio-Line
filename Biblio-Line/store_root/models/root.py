from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import Group, User

class Root(models.Model):
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=150)
    date_joined = models.DateTimeField(default=timezone.now)
    
    #to save the data
    def register(self):
        self.save()
        group = Group.objects.get(name = 'Administrador')
        user = User.objects.get(username = self.username)
        group.user_set.add(user)
        self.send_email()
       
    def send_email(self):
        # Dirección de correo electrónico del destinatario
        addessee = self.email

        # Asunto del correo electrónico
        subject = 'Bienvenido a nuestra plataforma'

        # Contenido del correo electrónico
        message = 'Hola {},\n\nBienvenido a nuestra plataforma. !Gracias por registrarte!. \n Se ha creado una contraseña temporal con su DNI \n!Favor Cambiala¡'.format(self.username)

        # Envía el correo electrónico y especifica el encoding en el message
        send_mail(subject, message, settings.EMAIL_HOST_USER,   [addessee])
    
    def change_password(self, new_password):
        self.password = new_password
        self.save()

    @staticmethod
    def get_root():
        try:
            return Root.objects.get(username = 'root')
        except:
            return False


    class Meta:
        db_table = 'auth_user'
        managed = False
    