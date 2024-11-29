from django.urls import path

from leaderboard.views import LeaderboardApiView

app_name = 'leaderboard'

urlpatterns = [
    path('', LeaderboardApiView.as_view(), name='leaderboard-list'),
]