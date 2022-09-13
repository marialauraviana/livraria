from rest_framework.viewsets import ModelViewSet
##from rest_framework.permissions import IsAuthenticated

from core.models import Categoria, Editora, Autor, Livro
from core.serializers import CategoriaSerializer
from core.serializers import EditoraSerializer
from core.serializers import AutorSerializer
from core.serializers import LivroSerializer

class CategoriaViewSet (ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
##  permission_classes = [IsAuthenticated]

class EditoraViewSet (ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet (ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
        
