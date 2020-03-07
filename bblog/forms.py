from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        # Modelo que tiene que usar para este form
        model = Post
        fields = ('title', 'text',)
