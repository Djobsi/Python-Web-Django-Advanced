from django.urls import path

from middlewares_sessions_cookies_demos.web.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)
