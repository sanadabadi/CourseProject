from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id}: {self.title}"

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    renter_name = models.CharField(max_length=100)
    renter_phone = models.CharField(max_length=15)
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Rental ID: {self.id}, Book: {self.book.title}, Renter: {self.renter_name}"
