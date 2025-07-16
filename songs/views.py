from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Song
from .serializers import SongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access
