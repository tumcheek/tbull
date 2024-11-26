from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'wallet']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True, 'min_length': 8},
        }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)