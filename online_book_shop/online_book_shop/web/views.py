from django.contrib.auth import get_user_model
from django.shortcuts import render

from online_book_shop.accounts.models import Profile
from django.utils import timezone
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from online_book_shop.books.models import Books
from online_book_shop.web.forms import ContactForm

UserModel = get_user_model()


def home(request):
    # recent_books = Books.objects.filter(publication_date__lte=timezone.now()).order_by('-id')[:5]
    recent_books = Books.objects.order_by('-id')[:5]
    profile = UserModel.objects.first()

    context = {
        "profile": profile,
        "recent_books": recent_books,
    }

    return render(request, "web/home_page.html", context)


def about_us(request):
    context = {

    }

    return render(request, "web/about_us_page.html", context)


def contacts(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            subject = 'Ново съобщение от "Online Book Shop"'
            message = f'Name: {form.cleaned_data["your_name"]}\nEmail: {form.cleaned_data["from_email"]}\nMessage: {form.cleaned_data["message"]}'
            send_mail(subject, message, 'alex.kitanovv@gmail.com', ['alex.kitanovv@gmail.com'])
            form.save()
            return redirect("home-page")

    context = {
        "form": form,
    }

    return render(request, "web/contact_page.html", context)


def search_books(request):
    author = request.GET.get('author')
    if author:
        # Filter books by author
        books = Books.objects.filter(author__icontains=author)
    else:
        books = Books.objects.all()

    context = {'books': books}
    return render(request, 'web/search_results.html', context)


