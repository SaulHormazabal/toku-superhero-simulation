from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import CharacterStatisticsSerializer
from .serializers import AlignmentStatisticsSerializer

from .models import CharacterStatistics, AlignmentStatistics


class CharacterStatisticsListView(ListAPIView):
    queryset = CharacterStatistics.objects.all()
    serializer_class = CharacterStatisticsSerializer


class CharacterStatisticsRetrieveView(RetrieveAPIView):
    queryset = CharacterStatistics.objects.all()
    serializer_class = CharacterStatisticsSerializer


class AlignmentStatisticsListView(ListAPIView):
    queryset = AlignmentStatistics.objects.all()
    serializer_class = AlignmentStatisticsSerializer


class AlignmentStatisticsRetrieveView(RetrieveAPIView):
    queryset = AlignmentStatistics.objects.all()
    serializer_class = AlignmentStatisticsSerializer
