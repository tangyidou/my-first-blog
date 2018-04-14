from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from oneblog.forms import ArticleForm
from oneblog.models import Article


def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'oneblog/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'oneblog/article_detail.html', {'article': article})


def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'oneblog/article_edit.html', {'form': form})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'oneblog/article_edit.html', {'form': form})