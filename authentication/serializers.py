from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'wallet', 'coins']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True, 'min_length': 8},
        }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UpdateCoinsSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def validate(self, data):
        user = self.context['request'].user
        amount = data.get('amount', 0)

        if user.coins + amount < 0:
            raise serializers.ValidationError("Insufficient coins to perform this operation.")
        return data

    def update(self, instance, validated_data):
        amount = validated_data.get('amount', 0)
        instance.coins += amount
        instance.save()
        return instance