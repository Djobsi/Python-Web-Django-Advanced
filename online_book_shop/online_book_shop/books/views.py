from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse

from online_book_shop.accounts.models import Profile
from online_book_shop.books.forms import BooksForm, DeleteBookForm
from online_book_shop.books.models import Books, ShoppingCart


@login_required
def create_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book_owner = get_user_model().objects.get(pk=request.user.pk)
            book.book_owner = book_owner
            book.save()
            return redirect('home-page')
    else:
        form = BooksForm()

    context = {
        'form': form
    }
    return render(request, 'books/create_books.html', context)


def book_details(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.user.is_authenticated:
        profile = Profile.objects.get_or_create(user=request.user)
    else:
        profile = request.user

    print(request.user.pk)
    print(book.book_owner.pk)

    context = {
        'profile': profile,
        'book': book,
    }

    return render(request, template_name='books/details_book.html', context=context)


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Books, pk=pk)

    if request.method == "POST":
        form = BooksForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('details-book-page', kwargs={'pk': pk}))
    else:
        form = BooksForm(instance=book)

    context = {
        "form": form,
        "book": book,
    }

    return render(request, "books/edit_book_page.html", context)


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Books, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('home-page')
    else:
        form = DeleteBookForm(instance=book)

    context = {
        'book': book,
        'form': form,
    }

    return render(request, 'books/delete_books.html', context)


@login_required
def add_to_cart(request, pk):
    book = get_object_or_404(Books, pk=pk)
    shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    shopping_cart.books.add(book)

    return redirect('home-page')


@login_required
def view_cart(request):
    shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_items = shopping_cart.books.all()
    total_price = sum(item.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)


@login_required
def proceed_to_checkout(request):
    shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_items = shopping_cart.books.all()
    total_price = sum(item.price for item in cart_items)
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        if profile.profile_money >= total_price:
            profile.profile_money -= total_price
            profile.save()

            for item in cart_items:
                book_owner_profile = item.book_owner.profile
                book_owner_profile.profile_money += item.price
                book_owner_profile.save()

            shopping_cart.books.clear()

            return redirect('home-page')

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'profile': profile,
    }
    return render(request, 'cart/proceed_to_checkout.html', context)


@login_required
def remove_from_cart(request, pk):
    book = get_object_or_404(Books, pk=pk)
    shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    shopping_cart.books.remove(book)
    return redirect('view-cart-page')



