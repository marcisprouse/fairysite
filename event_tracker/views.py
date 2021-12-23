from django.shortcuts import render
from event_tracker.serializers import EventSerializer
from event_tracker.models import Event
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
