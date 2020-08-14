from rest_framework import viewsets, permissions
from api_blog.models import Phrases
from api_blog.serializers import PhrasesSerializer


class PhrasesViewSets(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PhrasesSerializer
    queryset = Phrases.objects.all()
