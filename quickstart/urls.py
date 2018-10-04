from django.conf.urls import url
from quickstart import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]