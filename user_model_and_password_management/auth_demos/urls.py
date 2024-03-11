from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login', LoginView.as_view(), name='login'),
]
