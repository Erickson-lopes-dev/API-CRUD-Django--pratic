from rest_framework import viewsets
from api_blog.models import Phrases
from api_blog.serializers import PhrasesSerializer


class PhrasesViewSets(viewsets.ModelViewSet):
    serializer_class = PhrasesSerializer
    queryset = Phrases.objects.all()
