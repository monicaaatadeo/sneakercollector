from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sneakers/', views.sneakers_index, name='index'),
  path('sneakers/new/', views.new_sneaker, name='new_sneaker'),
  path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name = 'detail'),
  path('sneakers/<int:sneaker_id>/edit/', views.sneakers_update, name='sneakers_update'),
  path('sneakers/<int:sneaker_id>/delete/', views.sneakers_delete, name='sneakers_delete'),
  path('sneakers/<int:sneaker_id>/add_wearing/', views.add_wearing, name = 'add_wearing'),
  path('sneakers/<int:sneaker_id>/assoc_box/<int:box_id>/', views.assoc_box, name='assoc_box'),
  
# FULL CRUD
  path('boxes/', views.BoxList.as_view(), name='boxes_index'),
  path('boxes/<int:pk>/', views.BoxDetail.as_view(), name='boxes_detail'),
  path('boxes/create/', views.BoxCreate.as_view(), name='boxes_create'),
  path('boxes/<int:pk>/update/', views.BoxUpdate.as_view(), name='boxes_update'),
  path('boxes/<int:pk>/delete/', views.BoxDelete.as_view(), name='boxes_delete'),
	]