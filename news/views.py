from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView


from news.models import News
from news.serializers import NewsSerializer



class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @swagger_auto_schema(manual_parameters=[openapi.Parameter(
        name='last',
        in_=openapi.IN_QUERY,
        description='The number of last news',
        type=openapi.TYPE_INTEGER,
        required=False,
    ), ])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        last = self.request.GET.get('last', None)
        news = News.objects.all().order_by('-created_at')
        if last is not None:
            try:
                last = int(last)
            except ValueError:
                last = None
        return news[:last] if last else news
