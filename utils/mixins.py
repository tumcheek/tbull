from rest_framework import status
from rest_framework.response import Response


class ResponseMixin:
    """
    A mixin that provides reusable response methods for DRF views.
    """

    def unauthorized_response(self, message="Authentication credentials were not provided."):
        """
        Returns a 401 Unauthorized response.
        """
        return Response({"detail": message}, status=status.HTTP_401_UNAUTHORIZED)