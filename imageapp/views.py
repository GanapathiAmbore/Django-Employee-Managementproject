from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import ListView, CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy # new
from .forms import PostForm # new
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Update(UpdateView):
    model = Post
    fields = '__all__'
    template_name ='update.html'
    success_url = reverse_lazy('home')

class Delete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

