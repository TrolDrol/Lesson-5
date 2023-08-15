from django.shortcuts import render # Для отправки HTML по запросу пользователя
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse('Успешно')
def index(request):
    return render(request, "index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")