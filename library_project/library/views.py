from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Rental
from .forms import BookForm, RentalForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def rent_book(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.book.available_copies -= 1
            rental.book.save()
            rental.save()
            return redirect('rental_list')
    else:
        form = RentalForm()
    return render(request, 'library/rent_book.html', {'form': form})

def return_book(request):
    if request.method == 'POST':
        rental_id = request.POST.get('rental_id')
        rental = get_object_or_404(Rental, id=rental_id, return_date__isnull=True)
        rental.return_date = datetime.now()
        rental.save()
        rental.book.available_copies += 1
        rental.book.save()
        return redirect('rental_list')
    return render(request, 'library/return_book.html')

def rental_list(request):
    rentals = Rental.objects.all()
    return render(request, 'library/rental_list.html', {'rentals': rentals})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/update_book.html', {'form': form, 'book': book})
