from django.urls import path

from online_book_shop.web.views import home, about_us, contacts, search_books

urlpatterns = (
    path("", home, name="home-page"),
    path("about-us/", about_us, name="about-us-page"),
    path("contact-us/", contacts, name="contact-us-page"),
    path("search/book/", search_books, name="search-books"),
)

