from django.urls import path

from .views import CharacterStatisticsListView, CharacterStatisticsRetrieveView
from .views import AlignmentStatisticsListView, AlignmentStatisticsRetrieveView


urlpatterns = [
    path('metrics/characters/', CharacterStatisticsListView.as_view()),
    path('metrics/characters/<int:pk>/', CharacterStatisticsRetrieveView.as_view()),
    path('metrics/alignments/', AlignmentStatisticsListView.as_view()),
    path('metrics/alignments/<int:pk>/', AlignmentStatisticsRetrieveView.as_view()),
]
