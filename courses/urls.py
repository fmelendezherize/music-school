from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^instruments/$', views.InstrumentList.as_view()),
    url(r'^departments/$', views.DepartmentList.as_view()),
]