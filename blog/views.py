from django.shortcuts import render

from django.views.generic import ListView, DetailView 
"""
    importing Listview and Detailview for using class views and it also useful for database quries
"""
from .models import Post



# def home(request):
#     return render(request, 'index.html')


class HomeView(ListView):
    modeel = Post
    template_name = 'index.html'