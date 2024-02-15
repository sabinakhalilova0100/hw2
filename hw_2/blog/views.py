from django.shortcuts import render
from .models import Article
# Create your views here.

def get_index_page(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def get_article_details(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'blog/article-details.html', {'article': article})


# Create your views here.
