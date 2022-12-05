from django import forms
from .models import Comment

# class CommentForm(forms.Form):

#     comment = forms.CharField(max_length=300)
#     email = forms.EmailField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'