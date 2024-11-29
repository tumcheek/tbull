from rest_framework.generics import ListAPIView


from news.models import News
from news.serializers import NewsSerializer


class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        last = self.request.GET.get('last', None)
        news = News.objects.all().order_by('-created_at')
        if last is not None:
            try:
                last = int(last)
            except ValueError:
                last = None
        return news[:last] if last else news
