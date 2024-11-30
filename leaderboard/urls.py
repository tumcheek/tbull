from django.urls import path

from leaderboard.views import LeaderboardApiView, LeaderboardMyRankApiView

app_name = 'leaderboard'

urlpatterns = [
    path('', LeaderboardApiView.as_view(), name='leaderboard-list'),
    path('rank/', LeaderboardMyRankApiView.as_view(), name='leaderboard-rank'),
]