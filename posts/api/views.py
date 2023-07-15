from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import PostSerializer
from categories.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = PostSerializer
    # Mostrará todos los posts que esten publicados(published=True)
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    # Filtramos por categoria
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category'] en el navegador se añade  al endpoint /?category={categoria}
    filterset_fields = ['category__slug'] # se añade al endpoint /?category__slug={slug}





