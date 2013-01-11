from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from education import views


urlpatterns = patterns('api',
    url(r'^education/$', include('education.urls')),
    # url(r'^education/(?P<pk>[0-9]+)/$', views.EducationView.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)
