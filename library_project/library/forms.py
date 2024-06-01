from django import forms
from .models import Book, Rental

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'available_copies']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['book', 'renter_name', 'renter_phone']
