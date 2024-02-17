from rest_framework.viewsets import ModelViewSet
from authentification.serializer import UserSerializer
from authentification.models import User

from .permissions import IsAdminOrIsSelf


class UserViewSet(ModelViewSet):
    """
    View class to get all user
    """

    permission_classes = [IsAdminOrIsSelf]
    serializer_class = UserSerializer

    def get_queryset(self):

        return User.objects.all()
