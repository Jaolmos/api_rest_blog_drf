from rest_framework import serializers
from users.models import User 


class UserRegisterSerializer(serializers.ModelSerializer):
    """ Serializador para registrar usuarios """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


    # encriptamos el password de usuario
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        # Validamos que el password no venga vacio
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """ Serializador para obtener los datos del usuario """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']



class UserUpdateSerializer(serializers.ModelSerializer):
    """ Serializador para actualizar los datos del usuario """
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
