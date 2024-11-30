from django.db import transaction
from django.db.models import Window, F, Subquery
from django.db.models.functions import Rank
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from leaderboard.models import Leaderboard
from leaderboard.serializers import LeaderboardSerializer
from utils.mixins import ResponseMixin


class LeaderboardApiView(ResponseMixin,ListCreateAPIView):
    """
    API view to retrieve the list of leaderboards or create a new leaderboard entry.
    """
    queryset = Leaderboard.objects.select_related('user').order_by('-score')
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create_or_update(self, request, *args, **kwargs):
        """
        Create a new leaderboard entry or update the existing one for the authenticated user.
        Update occurs only if the new score is higher than the current score.
        """
        user = request.user
        new_score = request.data.get('score')

        if new_score is None:
            return Response(
                {"detail": "Score is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            with transaction.atomic():
                leaderboard_entry = Leaderboard.objects.select_for_update().get(user=user)

                if new_score > leaderboard_entry.score:
                    serializer = self.get_serializer(
                        leaderboard_entry, data={'score': new_score}, partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    self.perform_update(serializer)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    serializer = self.get_serializer(leaderboard_entry)
                    return Response(
                        serializer.data,
                        status=status.HTTP_200_OK,
                        headers=self.get_success_headers(serializer.data),
                    )
        except Leaderboard.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        Assign the authenticated user to the leaderboard entry upon creation.
        """
        serializer.save(user=self.request.user)


    def create(self, request, *args, **kwargs):
        """
        Override the default create method to handle create or update logic.
        """
        if not request.user.is_authenticated:
            return self.unauthorized_response()
        return self.create_or_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        """
        Save the updated leaderboard entry.
        """
        serializer.save()



class LeaderboardMyRankApiView(ResponseMixin, APIView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.unauthorized_response()

        ranked_leaderboard = Leaderboard.objects.annotate(
            rank=Window(
                expression=Rank(),
                order_by=F('score').desc()
            )
        )

        ranks = list(filter(lambda record: record.user == request.user, ranked_leaderboard))

        user_rank = ranks[0].rank if ranks else None

        return Response({'rank': user_rank})