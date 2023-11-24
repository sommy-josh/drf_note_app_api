from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import NoteApp

from .serializers import NoteSerializer

# Create your views here.
class CreateNote(generics.ListCreateAPIView):
    queryset=NoteApp.objects.all()
    serializer_class= NoteSerializer

class UpdateNote(generics.RetrieveUpdateDestroyAPIView):
    queryset=NoteApp.objects.all()
    serializer_class=NoteSerializer
