from rest_framework import serializers
from users.models import User 


class UserRegisterSerializer(serializers.ModelSerializer):
    """ Serializador para registrar usuarios """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


