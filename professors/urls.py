from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^professors/$', views.ProfessorList.as_view()),
    url(r'^professors/(?P<pk>[0-9]+)/$', views.ProfessorDetail.as_view()),
]