from django.contrib import admin
from oneblog import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'text', 'created_date', 'published_date' ]
    search_fields = ['title', 'text']
    list_filter = ['author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'author', 'created_date', 'article' ]
    search_fields = ['content']
    list_filter = ['author', 'article']


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
