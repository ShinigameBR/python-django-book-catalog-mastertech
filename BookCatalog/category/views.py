from django.shortcuts import render
from django.views.generic import ListView, DetailView
from category.models import Category

class CategoryListView(ListView):
    model = Category
    template_name = "category/home.html"
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category/category_detail.html"