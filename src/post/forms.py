# coding: utf-8
from django import forms


class PostsListForm(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('author', 'Автор'), ('created_at', u'Дата публикации')), required=False)

    def clean_search(self):
        search = self.cleaned_data.get('search')
        return search


class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)