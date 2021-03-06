from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from webapp.forms import BookForm
from webapp.models import Book


# Create your views here.

def index_view(request):
    books = Book.objects.all()
    return render(request, 'index.html', context={'books': books})


def book_view(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'book_view.html', context={'book': book})


def book_create_view(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'book_create.html', context={'form': form})
    elif request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(
                title=form.cleaned_data.get('title'),
                mail=form.cleaned_data.get('mail'),
                description=form.cleaned_data.get('description')
            )


        else:
            return render(request, 'book_create.html', context={'form': form})

        return redirect('book-view', pk=book.id)


def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(initial={
            'title': book.title,
            'mail': book.mail,
            'description': book.description,
        })
        return render(request, 'book_update.html', context={'form': form, 'book': book})
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.mail = form.cleaned_data['mail']
            book.description = form.cleaned_data['description']
            book.save()
            return redirect('book-view', pk=book.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'book': book})


def book_delete_view(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'GET':
        return render(request, 'book_delete.html', context={'book': book})
    elif request.method == 'POST':
        book.delete()
    return redirect('book-list')
