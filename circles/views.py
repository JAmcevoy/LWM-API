from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, InterestCircle
from .serializers import CategorySerializer, InterestCircleSerializer
from learnwithme.permissions import IsOwnerOrReadOnly


class CategoryList(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(
            category, many=True, context={'request': request}
        )
        return Response(serializer.data)

class InterestCircleList(generics.ListCreateAPIView):
    serializer_class = InterestCircleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return InterestCircle.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InterestCircleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InterestCircle.objects.all()
    serializer_class = InterestCircleSerializer
    permission_classes = [IsOwnerOrReadOnly]
