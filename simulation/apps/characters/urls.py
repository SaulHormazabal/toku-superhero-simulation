from django.urls import path

from .views import (
    CharacterListView,
    CharacterAlignmentListView,
    CharacterAlignmentRetrieveView,
    CharacterRetrieveView,
)


urlpatterns = [
    path('characters/', CharacterListView.as_view()),
    path('characters/<int:pk>/', CharacterRetrieveView.as_view()),
    path('character-alignments/', CharacterAlignmentListView.as_view()),
    path('character-alignments/<int:pk>/', CharacterAlignmentRetrieveView.as_view()),
]
