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


class InterestCircleList(APIView):
    def get(self, request):
        interest = InterestCircle.objects.all()
        serializer = InterestCircleSerializer(
            interest, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = InterestCircleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterestCircleDetail(APIView):
    serializer_class = InterestCircleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            interest = InterestCircle.objects.get(pk=pk)
            self.check_object_permissions(self.request, interest)
            return interest
        except InterestCircle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        interest = self.get_object(pk)
        serializer = InterestCircleSerializer(
            interest, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        interest = self.get_object(pk)
        serializer = InterestCircleSerializer(
            interest, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
