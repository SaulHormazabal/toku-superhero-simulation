from rest_framework import generics

from .models import Fight
from .serializers import FightSerializer
from .tasks import simulate_fight


class FightCreateView(generics.CreateAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer

    def perform_create(self, serializer):
        serializer.save()
        simulate_fight.delay(fight_id=serializer.data['id'])


class FightRetrieveView(generics.RetrieveAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer


class FightListView(generics.ListAPIView):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    filterset_fields = (
        'winner__alignment',
        'winner__alignment__name',
        'loser__alignment',
        'loser__alignment__name',
    )
    ordering_fields = (
        'id',
        'turns',
        'created_at',
        'updated_at',
    )
