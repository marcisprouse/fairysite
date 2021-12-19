from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=25)
    email = forms.EmailField(label='Your Email')
    to = forms.EmailField(label='To Email')
    comments = forms.CharField(label='Your Message', required=False,
                               widget=forms.Textarea(attrs={
                              'style': 'height: 200px;width:300px'}),)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField(label="")
