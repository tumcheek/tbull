from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewSet(CreateModelMixin,GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user