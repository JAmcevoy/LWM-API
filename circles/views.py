from rest_framework import generics, permissions
from learnwithme.permissions import IsOwnerOrReadOnly
from .models import Category, InterestCircle
from .serializers import CategorySerializer, InterestCircleSerializer

class CategoryList(generics.ListAPIView):
    """
    API view to list all categories.
    - GET: Retrieve a list of all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class InterestCircleList(generics.ListCreateAPIView):
    """
    API view to list all interest circles or create a new one.
    - GET: Retrieve a list of all interest circles.
    - POST: Create a new interest circle.
    """
    serializer_class = InterestCircleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Return a list of all interest circles.
        """
        return InterestCircle.objects.all()

    def perform_create(self, serializer):
        """
        Save the new interest circle with the current user as the owner.
        """
        serializer.save(owner=self.request.user)

class InterestCircleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific interest circle.
    - GET: Retrieve an interest circle by its ID.
    - PUT/PATCH: Update an interest circle.
    - DELETE: Delete an interest circle.
    """
    queryset = InterestCircle.objects.all()
    serializer_class = InterestCircleSerializer
    permission_classes = [IsOwnerOrReadOnly]
