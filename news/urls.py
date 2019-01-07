from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from news.models import Articles
from . import views

urlpatterns = [
    url('^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],template_name="news/articles.html")),
]
