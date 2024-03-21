from django.http import HttpResponse
from django.urls import path

from django_rest_basics.web.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)
