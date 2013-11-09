from goudimel.models.piece import Piece
from goudimel.serializers.book import BookSerializer

from rest_framework import serializers

class PieceSerializer(serializers.HyperlinkedModelSerializer):
    book_id = BookSerializer()
    composer_name = serializers.Field(source="composer_name")

    class Meta:
        model = Piece
