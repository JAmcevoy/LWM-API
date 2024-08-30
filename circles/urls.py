from django.urls import path
from circles import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('interest-circles/', views.InterestCircleList.as_view()),
    path('interest-circles/<int:pk>/', views.InterestCircleDetail.as_view()),
]