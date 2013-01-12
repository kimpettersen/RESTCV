from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from RESTCV.api.education import views


urlpatterns = patterns('RESTCV.api.education',
    url(r'^', views.EducationList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.EducationView.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)
