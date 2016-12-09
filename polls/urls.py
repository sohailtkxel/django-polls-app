from django.conf.urls import url

from . import views
urlpatterns = [
    # Django wants to parse the given positional argument as the keyword argument kwargs, and since a string is an
    # iterable, an atypical code path begins to unfold. Always use name= in your url third parameter!
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
]
