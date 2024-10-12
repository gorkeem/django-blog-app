from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_page, name='post_page')
]
