from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # Se sustituye id por slug para buscar o indicar la categoria
    lookup_field = 'slug'
