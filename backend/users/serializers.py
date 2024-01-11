from rest_framework import serializers
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        """
        Faz com que a senha seja passada na
        criação do usuário, mas não nas requisições
        para a API.
        """
        password = validated_data.pop('password')
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user
