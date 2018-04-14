from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from oneblog.models import Article


def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'oneblog/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'oneblog/article_detail.html', {'article': article})
