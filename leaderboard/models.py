from django.db import models

from authentication.models import User


class Leaderboard(models.Model):
    score = models.PositiveIntegerField(default=0, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}: {self.score}'