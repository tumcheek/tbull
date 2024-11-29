from rest_framework import serializers

from leaderboard.models import Leaderboard


class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['username', 'score']