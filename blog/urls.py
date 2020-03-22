from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('ppl', views.alum_list, name='alum_list')
]