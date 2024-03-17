from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("middlewares_sessions_cookies_demos.web.urls")),
]
