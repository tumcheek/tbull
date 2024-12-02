from rest_framework.generics import ListAPIView


from news.models import News
from news.pagination import NewsPagination
from news.serializers import NewsSerializer



class NewsListApiView(ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
