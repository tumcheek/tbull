from django.urls import path
from rest_framework.routers import DefaultRouter

from authentication.views import UserViewSet, UserMeView

app_name = 'authentication'

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")


urlpatterns = [path('users/me/', UserMeView.as_view(), name='me')]

urlpatterns += router.urls