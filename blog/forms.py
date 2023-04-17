from .models import Comment
from django import forms
from django.forms import ModelForm
from .models import Post
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    """
    Form to add a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "featured_image",
        )

    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "author": forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "hidden"
            }
        ),
        "destinations": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(
            attrs={
                "class": "form-control",
                "placeholder": "Add your content here",
            }
        ),
    }

class UpdatePostForm(forms.ModelForm):
    """
    Form to edit a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "excerpt",
            "content",
            "featured_image",
        )
    
    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "excerpts": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(attrs={"class": "form-control"}),
    }