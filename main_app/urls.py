from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('parrots/', views.parrots_index, name='index'),
    path('parrots/<int:parrot_id>/', views.parrots_detail, name='detail'),
    path('parrots/create/', views.ParrotCreate.as_view(), name='parrots_create'),
    path('parrots/<int:pk>/update/', views.ParrotUpdate.as_view(), name='parrots_update'),
    path('parrots/<int:pk>/delete/', views.ParrotDelete.as_view(), name='parrots_delete'),
    path('parrots/<int:parrot_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('parrots/<int:parrot_id>/assoc_jacket/<int:jacket_id>/', views.assoc_jacket, name='assoc_jacket'),
    path('jackets/', views.JacketList.as_view(), name='jackets_index'),
    path('jackets/<int:pk>/', views.JacketDetail.as_view(), name='jackets_detail'),
]