from rest_framework import serializers
from authentification.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating user, whith overrided create fonction for age validation
    """

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
        extra_kwarg = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        if validated_data["birthdate"] <= 15:
            raise serializers.ValidationError(
                "You must be older than 15 to use our service"
            )
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data):
        instance.can_data_be_shared = validated_data["can_data_be_shared"]
        instance.can_be_contacted = validated_data["can_be_contacted"]
        instance.birthdate = validated_data["birthdate"]
        instance.set_password(validated_data["password"])
        return instance
