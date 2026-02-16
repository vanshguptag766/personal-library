from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from django.db.models import Q
from .models import Book
from .forms import BookForm

def home(request):
    total_books = Book.objects.count()
    context = {
        'total_books': total_books,
    }
    return render(request, 'home.html', context)

def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, 'Book added successfully!')
            return redirect('home')
        else:
            error(request, 'There was an error adding the book.')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'addbook.html', context)

def delbook(request, id=None):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        book_title = book.title
        book.delete()
        success(request, f'Book "{book_title}" deleted successfully!')
        return redirect('home')
    
    if id:
        book = get_object_or_404(Book, id=id)
        context = {'book': book}
        return render(request, 'delbook.html', context)
    
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'delbook.html', context)

def updatebook(request, id=None):
    if id:
        book = get_object_or_404(Book, id=id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                success(request, f'Book "{book.title}" updated successfully!')
                return redirect('home')
            else:
                error(request, 'There was an error updating the book.')
        else:
            form = BookForm(instance=book)
        context = {'form': form, 'book': book}
        return render(request, 'updatebook.html', context)
    
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'updatebooks.html', context)

def viewbooks(request):
    books = Book.objects.all()
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', '-created_at')
    
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(isbn__icontains=search_query)
        )
    
    books = books.order_by(sort_by)
    
    context = {
        'books': books,
        'search_query': search_query,
        'sort_by': sort_by,
        'total_books': Book.objects.count(),
        'result_count': books.count()
    }
    return render(request, 'viewbooks.html', context)
