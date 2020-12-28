from .models import COMMENT
from django import forms


class CommentForm(forms.ModelForm):
    author = forms.CharField(label='Name', max_length=100,required=True ,widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))

    email = forms.CharField(required=True, widget=forms.EmailInput
                            (attrs={'class': 'form-control', 'placeholder': 'Email'}))

    text = forms.CharField(required=True, label='Comment', max_length=1000,
                           widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}))

    class Meta:
        model = COMMENT
        fields = ['author', 'email', 'text']
