from django.urls import path
from .views import ChatList, ChatDetail

urlpatterns = [
    path('chats/circle/<int:circle_id>/', ChatList.as_view(), name='chat-list-create'),
    path('chats/<int:pk>/', ChatDetail.as_view(), name='chat-detail'),
]
