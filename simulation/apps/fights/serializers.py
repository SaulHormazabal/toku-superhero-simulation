from rest_framework import serializers

from .models import Fight


class FightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fight
        fields = '__all__'
        read_only_fields = [
            'winner',
            'loser',
            'turns',
            'created_at',
            'updated_at',
        ]
