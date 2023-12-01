from rest_framework import serializers

from .models import Character, CharacterAlignment


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterAlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterAlignment
        fields = '__all__'
