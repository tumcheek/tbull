from django.urls import path
from rest_framework.routers import DefaultRouter

from authentication.views import UserViewSet, UserMeView, UpdateCoinsView

app_name = 'authentication'

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")


urlpatterns = [path('users/me/', UserMeView.as_view(), name='me'),
               path('user/coins/', UpdateCoinsView.as_view(), name='update-coins'),
               ]

urlpatterns += router.urls