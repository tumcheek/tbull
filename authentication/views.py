from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from authentication.models import User
from authentication.serializers import UserSerializer, UpdateCoinsSerializer


class UserViewSet(CreateModelMixin,GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UpdateCoinsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateCoinsSerializer

    @swagger_auto_schema(request_body=UpdateCoinsSerializer)
    def patch(self, request, *args, **kwargs):
        serializer = UpdateCoinsSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            serializer.update(user, serializer.validated_data)
            return Response({'coins': user.coins}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)