

from django.forms import ModelForm, CharField, Textarea
from .models import Post, Comment

class PostForm(ModelForm):
    text = CharField(widget= Textarea, label='Entry')
    class Meta:
        model = Post
        exclude = ['author', 'slug']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
