from django.shortcuts import render
from django.http import HttpResponse
from news.models import SchoolNews

def index(request):
    school_news_list = SchoolNews.objects.all()

    context_dict = {}
    context_dict['news'] = school_news_list

    return render(request, 'news/index.html', context=context_dict)
