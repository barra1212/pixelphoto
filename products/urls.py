from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from .views import all_products, men, sports, women, upvote, downvote

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^men/', men, name='products_list_men'),
    url(r'^sports/', sports, name='products_list_sports'),
    url(r'^women/', women, name='products_list_women'),
    url(r'^upvote/(?P<product_id>[0-9]+)/$', upvote, name='upvote'),
    url(r'^downvote/(?P<product_id>[0-9]+)/$', downvote, name='downvote'),
]
