from rest_framework.serializers import ModelSerializer

from .models import CharacterStatistics, AlignmentStatistics


class CharacterStatisticsSerializer(ModelSerializer):
    class Meta:
        model = CharacterStatistics
        fields = '__all__'


class AlignmentStatisticsSerializer(ModelSerializer):
    class Meta:
        model = AlignmentStatistics
        fields = '__all__'
