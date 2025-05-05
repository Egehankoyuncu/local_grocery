from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('toggle-favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('filter-products/', views.filter_products, name='filter_products'),
    path('save-location/', views.save_location, name='save_location'),
] 