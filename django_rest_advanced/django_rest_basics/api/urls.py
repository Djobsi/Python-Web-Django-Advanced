from django.urls import path
from rest_framework.authtoken import views as token_views

from django_rest_basics.api.views import BookListCreateApiView, BookUpdateApiView, api_list_authors, LogInApiView, RegisterApiView

urlpatterns = (
    path("books/", BookListCreateApiView.as_view(), name="api_list_create_books"),
    path("books/<int:pk>/", BookUpdateApiView.as_view(), name="api_update_book"),
    path("authors/", api_list_authors, name="api_list_author"),
    path("accounts/token/", LogInApiView.as_view(), name="api_obtain_auth_token"),
    path("accounts/", RegisterApiView.as_view(), name="api_user_create"),
)
