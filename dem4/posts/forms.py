from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ('author', )


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('author', 'post')
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }