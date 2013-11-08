from goudimel.models.phrase import Phrase
from rest_framework import serializers

class PhraseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Phrase