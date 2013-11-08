from goudimel.models.piece import Piece
from rest_framework import serializers

class PieceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Piece