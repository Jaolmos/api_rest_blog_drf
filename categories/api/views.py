from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer

    #Devuelve todas las categorias
    queryset = Category.objects.all()

    # Devuelve todas las categorias que tengan published=True
    queryset = Category.objects.filter(published=True)

    # Se sustituye id por slug para buscar o indicar la categoria
    lookup_field = 'slug'
    # Sistemas de filtros de django
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
