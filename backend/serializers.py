from rest_framework import serializers

from .models import Note


class UserNoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Note
        fields = ["id", "user", "title", "content", "created_at", "updated_at"]
    
    def create(self, validated_data):
        user = self.context["user"]
        return Note.objects.create(user_id=user.id, **validated_data)