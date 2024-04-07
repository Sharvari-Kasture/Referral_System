from django.urls import path
from .import views

urlpatterns = [
    path('user-registration/', views.user_registration),
    path('user-details/', views.user_details),
    path('referrals/', views.referrals),
]
