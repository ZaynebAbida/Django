from unittest import loader
from django.shortcuts import render

from blog.forms import PostForm
from .models import Post 


from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class ListePosts(ListView):
    model = Post
    template_name = 'blog/listPost.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detailPost.html'
    context_object_name = 'post'


class CreerPost(CreateView):
    model = Post
    template_name = 'blog/creerPost.html'
    form_class = PostForm
    success_url = reverse_lazy('listPosts')
    def from_valid(self , form):
        self.objet= form.save()
        return super().from_valid(form)


class ModifierPost(UpdateView):
    model = Post
    template_name = 'blog/modifierPost.html'
    form_class = PostForm
    success_url = reverse_lazy('listPosts')



class SupprimerPost(DeleteView):
    model = Post
    template_name = 'blog/supprimerPost.html'
    success_url = reverse_lazy('listPosts')