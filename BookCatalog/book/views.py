from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Book
from category.models import Category
from user.models import CustomUser
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = 'books'


class HomeListView(ListView):
    model = Book
    template_name = "book/home.html"
    context_object_name = 'books'
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[
            :5]
        context['users'] = CustomUser.objects.all()[:5]
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_detail.html"


class BorrowBtn(LoginRequiredMixin, View):
    template_name = 'book/home.html'

    def post(self, request,  * args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        book.return_date = request.POST["return_date"]
        if book.copies > 0 and request.user not in book.users.all():
            book.copies -= 1
            if book.copies == 0:
                book.status = 'Indisponível'
            custom_user = request.user
            book.users.add(custom_user)
            book.save()
        else:
            messages.error(request, 'Desculpe, este livro não possui mais exemplares disponíveis.')
            
        return redirect('book:book_detail', kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return redirect('book:book')


class ReturnBtn(LoginRequiredMixin, View):

    def post(self, request,  * args, **kwargs):

        book = get_object_or_404(Book, pk=kwargs['pk'])
        if request.user in book.users.all():
            book.copies +=1
            book.status = 'Disponível'
            book.return_date = None
            book.users.remove(request.user)
            book.save()
        else:
            messages.error(request, 'Desculpe, este livro não tem nenhum exemplar em sua posse.')

        return redirect('book:book_detail', kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return redirect('book:book')


class Search(View):
    def post(self, request,  * args, **kwargs):
        searchname = request.POST["search"]
        if searchname == '':
            return redirect('book:book')
        books = Book.objects.filter(title__startswith=searchname)
        books = books | Book.objects.filter(author__startswith=searchname)
        users = []
        if request.user.is_staff:
            users = CustomUser.objects.filter(
                first_name__startswith=searchname)
        return render(request, 'book/search.html', {'users': users, 'books': books})

    def get(self, request, *args, **kwargs):

        return redirect('book:book')