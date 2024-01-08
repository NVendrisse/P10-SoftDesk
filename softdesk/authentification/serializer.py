from rest_framework.serializers import ModelSerializer
from authentification.models import User


class UserSerializer(ModelSerializer):
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
        return User.objects.create_user(**validated_data)
