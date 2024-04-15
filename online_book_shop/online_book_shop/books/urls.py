from django.urls import path, include

from online_book_shop.books.views import create_book, book_details, edit_book, delete_book, add_to_cart, view_cart,\
    proceed_to_checkout, remove_from_cart

urlpatterns = (
    path("create/", create_book, name="create-books"),
    path(
        "/<int:pk>/", include([
            path("details/", book_details, name="details-book-page"),
            path("edit/", edit_book, name="edit-book-page"),
            path("delete/", delete_book, name="delete-book-page"),
            path("cart/", add_to_cart, name="add-to-cart-page"),
        ]),
    ),
    path("remove-from-cart/<int:pk>", remove_from_cart, name="remove-from-cart"),
    path("cart/", view_cart, name="view-cart-page"),
    path("checkout/", proceed_to_checkout, name="proceed-to-checkout"),
)
