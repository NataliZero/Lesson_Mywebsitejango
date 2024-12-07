from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')  # Главная страница

def page1(request):
    return render(request, 'main/page1.html')  # Страница 1

def page2(request):
    return render(request, 'main/page2.html')  # Страница 2

def page3(request):
    return render(request, 'main/page3.html')  # Страница 3
