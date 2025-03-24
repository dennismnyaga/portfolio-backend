from django.urls import path
from . import views

urlpatterns = [
    path('', views.PorfolioViews.as_view()),
    path('portfolio/<str:pk>/', views.PorfolioDetailsViews.as_view()),
    path('email/', views.email_sender.as_view())
]
