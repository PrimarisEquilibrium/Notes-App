from django.urls import path

from .views import UserNoteView, DetailUserNoteView

urlpatterns = [
    path("", UserNoteView.as_view()),
    path("<str:pk>/", DetailUserNoteView.as_view())
]
