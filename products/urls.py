from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from .views import all_products, men, sports, women

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^men/', men, name='products_list_men'),
    url(r'^sports/', sports, name='products_list_sports'),
    url(r'^women/', women, name='products_list_women'),
]