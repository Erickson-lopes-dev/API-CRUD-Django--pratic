from api_blog.models import Phrases
from rest_framework import serializers


class PhrasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrases
        fields = ['pk', 'title', 'content', 'user_id', 'created']
