from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('parrots/', views.parrots_index, name='index'),
    path('parrots/<int:parrot_id>/', views.parrots_detail, name='detail'),
]