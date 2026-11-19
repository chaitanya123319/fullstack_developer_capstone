from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
    path('dealer-page/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealer-page/<int:dealer_id>/review/', views.post_review, name='post_review'),
]
