from rest_framework import generics

from .models import Character, CharacterAlignment
from .serializers import CharacterSerializer, CharacterAlignmentSerializer


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filterset_fields = (
        'alignment',
        'alignment__name',
    )
    ordering_fields = (
        'created_at',
        'updated_at',
    )


class CharacterAlignmentListView(generics.ListAPIView):
    queryset = CharacterAlignment.objects.all()
    serializer_class = CharacterAlignmentSerializer
    filterset_fields = (
        'name',
    )
    ordering_fields = (
        'created_at',
        'updated_at',
    )


class CharacterAlignmentRetrieveView(generics.RetrieveAPIView):
    queryset = CharacterAlignment.objects.all()
    serializer_class = CharacterAlignmentSerializer


class CharacterRetrieveView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
