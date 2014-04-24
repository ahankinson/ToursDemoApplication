from rest_framework import serializers
from goudimel.models.phrase import Phrase
from goudimel.serializers.piece import PieceSerializer

class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    piece_id = PieceSerializer()

    class Meta:
        model = Phrase