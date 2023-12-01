from django.urls import path

from .views import FightCreateView, FightRetrieveView, FightListView


urlpatterns = [
    path('fights/', FightListView.as_view()),
    path('fights/simulate/', FightCreateView.as_view()),
    path('fights/<int:pk>/', FightRetrieveView.as_view()),
]
