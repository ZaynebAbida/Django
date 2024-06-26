from .models import Post
from django.forms import ModelForm
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','content','status','image',"author"]
