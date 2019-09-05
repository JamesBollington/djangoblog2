from django import forms
from .models import Comment, Post
# Create your views here.
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('Name','Comment','Post')
        widgets ={'Post':forms.HiddenInput()}

class PostSearch(forms.ModelForm):
    class Meta:
        model=Post
        fields=('Title',)
