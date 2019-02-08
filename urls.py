from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit/$', views.handle_submission, name='submit'),
    url(r'^download/$', views.extract_as_csv, name='extract_as_csv')
]

