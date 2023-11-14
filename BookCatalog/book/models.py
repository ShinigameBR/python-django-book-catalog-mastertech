from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from category.models import Category
from django.core.validators import MinValueValidator 
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="books", null=True)
    users = models.ManyToManyField(
        get_user_model(), related_name="books", blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='book/images/', )
    copies = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    status = models.CharField(
        max_length=12,
        choices=[
            ("Disponível", "a"),
            ("Indisponível", "b")
        ], default="Disponível"
    )
    return_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:book_detail', args=[str(self.pk)])