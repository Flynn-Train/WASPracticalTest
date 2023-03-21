from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from .models import News

def index(request):


    news_list = News.objects.all()

    context_dict = {'news': news_list}

    return render(request, 'news/template1.html', context_dict)


