from django.urls import path

from news.views import NewsListApiView

app_name = 'news'



urlpatterns = [
    path('', NewsListApiView.as_view(), name='news_list'),
]