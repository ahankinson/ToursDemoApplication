from goudimel.models.book import Book
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book