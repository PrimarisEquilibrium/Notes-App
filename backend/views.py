from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Note
from .serializers import UserNoteSerializer
from .permissions import IsOwner


class UserNoteView(ListCreateAPIView):
    serializer_class = UserNoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Note.objects.select_related("user").filter(user_id=user_id)
    
    def get_serializer_context(self):
        return {"user": self.request.user}


class DetailUserNoteView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserNoteSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        note_id = self.kwargs["pk"]
        return Note.objects.filter(id=note_id)