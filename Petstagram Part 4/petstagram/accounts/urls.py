from django.urls import path, include

from petstagram.accounts.views import SignUpUserView, SignInUserView, ProfileDetailsView, EditProfileView, DeleteProfileView, \
    signout_user

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup-user"),
    path("signin/", SignInUserView.as_view(), name="signin-user"),
    path("signout/", signout_user, name="signout-user"),
    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="details-profile"),
            path("edit/", EditProfileView.as_view(), name="edit-profile"),
            path("delete/", DeleteProfileView.as_view(), name="delete-profile")
        ]),
    )
)
