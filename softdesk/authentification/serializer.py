from rest_framework import serializers
from authentification.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "birthdate",
            "password",
            "can_be_contacted",
            "can_data_be_shared",
        ]
        extra_kwarg = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data["birthdate"] <= 15:
            raise serializers.ValidationError(
                "You must be older than 15 to use our service"
            )
        return User.objects.create_user(**validated_data)
