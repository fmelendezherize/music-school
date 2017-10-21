from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^professors/$', views.ProfessorList.as_view()),
]