from django.urls import path, include

from online_book_shop.accounts.views import RegisterUserView, LoginUserView, logout_user, DetailsUserView, \
    UpdateUserView, ProfileDeleteView

urlpatterns = (
    path("register/", RegisterUserView.as_view(), name="register-page"),
    path("login/", LoginUserView.as_view(), name="login-page"),
    path("logout/", logout_user, name="logout-page"),

    path(
        "profile/<int:pk>/", include([
            path("", DetailsUserView.as_view(), name="details-page"),
            path("edit/", UpdateUserView.as_view(), name="edit-page"),
            path("delete/", ProfileDeleteView.as_view(), name="delete-page")
        ]),
    ),
)
