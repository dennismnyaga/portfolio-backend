from django.urls import path
from . import views

urlpatterns = [
    path('', views.PorfolioViews.as_view()),
    path('portfolio/<str:pk>/', views.PorfolioDetailsViews.as_view())
]
