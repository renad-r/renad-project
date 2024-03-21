from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_quote, name='add_quote'),
    path('quote/<int:quote_id>/', views.quote_detail, name='quote_detail'),
    path('profile/', views.profile, name='profile'),
]
