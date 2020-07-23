
from django.urls import path
from django.conf.urls import include, url
from news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article-year/(?P<pub_date>[^\.]+)$', views.year_archive, name='year_archive'),
    #url(r'^article/<int:year>/<int:month>/$', views.month_archive, name='month_archive'),
    url(r'^article-detail/(?P<article_id>[^\.]+)$', views.article_detail, name='article_detail'),

]