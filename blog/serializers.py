from rest_framework import serializers
from . import models


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ('id', 'artist', 'title', 'description')
