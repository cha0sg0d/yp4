from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ppl', views.alum_list, name='alum_list'),
    path('post/new/', views.alumni_new, name='alumni_new')
]