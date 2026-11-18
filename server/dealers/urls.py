
from django.urls import path
from . import views, auth_views

urlpatterns = [
    # Website pages
    path('', views.home, name='home'),
    path('dealer-page/<int:dealer_id>/', views.dealer_detail, name='dealer_detail'),
    path('dealer-page/<int:dealer_id>/review/', views.post_review, name='post_review'),

    # Dealer APIs
    path('dealers/', views.get_all_dealers),
    path('dealer/<int:dealer_id>/', views.get_dealer_by_id),
    path('dealers/state/<str:state>/', views.get_dealers_by_state),
    path('dealer/<int:dealer_id>/reviews/', views.get_dealer_reviews),
    path('dealer/<int:dealer_id>/reviews/submit/', views.create_dealer_review),

    # Authentication APIs
    path('register/', auth_views.register_user),
    path('login/', auth_views.login_user),
    path('logout/', auth_views.logout_user),
]
