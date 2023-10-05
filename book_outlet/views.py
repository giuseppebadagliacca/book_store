from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.


def index(request):
    # by which field you want to order by
    books = Book.objects.all().order_by("title")
    numb_books = books.count()
    # gets tge average for the rating fields
    average_rating = books.aggregate(Avg("rating"))

    return render(request,
                  "book_outlet/index.html",
                  {"books": books,
                   "total_number_of_books": numb_books,
                   "average_rating": average_rating
                   })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)

    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,
    })
