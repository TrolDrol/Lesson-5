from django.urls import path
from .views import index, test, top_sellers

urlpatterns = [
    path('', index, name='index'),
    path('top_sellers', top_sellers, name='top_sellers'),
]