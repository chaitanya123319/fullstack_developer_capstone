
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dealer-page/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealer-page/<int:dealer_id>/review/', views.post_review, name='post_review'),
]
