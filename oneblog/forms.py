from django import forms

from oneblog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text',)
