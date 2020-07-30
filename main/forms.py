from django import forms
from main import models
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title' , 'content' ,'image']
        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['content'].widget.attrs.update({ "class":"materialize-textarea"} , {"id":"textarea1"})
            self.fields['title'].widget.attrs.update({ "class":"validate"} ,{"id":"titlefield"})
            self.fields['image'].widget.attrs.update({ "class":"file-path validate"},{"id":"imageinput"})

class PostComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']

class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)