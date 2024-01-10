from rest_framework import serializers
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = [
            'id', 'name', 'username', 'email', 'sector', 'extension', 
            'gender','position', 'period', 'admission_date', 'theme_preference',
        ]