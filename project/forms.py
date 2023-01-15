from .models import Comment
from django import forms


class CommentForm(form.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
