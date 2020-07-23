from django.shortcuts import render, get_object_or_404
from news.models import Article, Reporter


def index(request):
    return render(request, 'news/index.html', {})

def year_archive(request, pub_date):
    a_list = Article.objects.filter(pub_date__year=2020)
    for a in a_list:
            year = a.pub_date
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    year = article.pub_date
    month = article.pub_date
    headline = article.headline
    reporter = article.reporter.full_name
    published_date = article.pub_date
    context = {
        'year': year, 'month': month, 'headline': headline,
       'reporter': reporter, 'published_date': published_date
    }
    return render(request, 'news/article_detail.html', context)

