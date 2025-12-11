from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def news(request):
    return render(request, 'news.html')

def news_detail(request):
    return render(request, 'news-detail.html')

def contact(request):
    return render(request, 'contact.html')
