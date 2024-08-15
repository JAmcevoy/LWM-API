from django.urls import path
from circles import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('interestcircles/', views.InterestCircleList.as_view()),
    path('interestcircles/<int:pk>/', views.InterestCircleDetail.as_view()),
]