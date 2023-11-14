from django import forms
from book.models import Book
from category.models import Category


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'description',  'img',
                  'category', 'copies']
        try:
            categories = Category.objects.all()
        except:
            categories = list()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'email text_box',
                'placeholder': 'Título',
                'id': 'title'}),
            'author': forms.TextInput(attrs={
                'class': 'email text_box',
                'placeholder': 'Autor',
                'id': 'title'}),
            'description': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Descrição',
                'id': 'title'}),
            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),
            'category': forms.Select(choices=categories, attrs={
                'class': 'email text_box',
                'placeholder': 'Categoria'}),
            'copies': forms.TextInput(attrs={
                'class': 'email text_box',
                'min': '1',
                'placeholder': 'Exemplares'}),
        }

        labels = {
            'title': '',
            'author': '',
            'description': '',
            'category': '',
            'img': '',
            'copies': '',
        }


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'img']

        help_texts = {
             'title': 'IMAGEM PARA CATEGORIA',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'email text_box ',
                'placeholder': 'Título ',
                'id': 'title'}),

            'img': forms.FileInput(attrs={
                'class': 'email text_box',
                'id': 'username'}),
        }
        labels = {
            'title': '',
            'img': '',
        }