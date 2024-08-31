from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response


class CreateNoteView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer 

class FetchNoteView(generics.RetrieveAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

class QueryNotesView(generics.ListAPIView):
    
    serializer_class=NoteSerializer
    
    def get_queryset(self):
        title_substring=self.request.query_params.get('title',None)
        if title_substring:
            return Note.objects.filter(title__icontains=title_substring)
        return Note.objects.all()
    

class UpdateNoteView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer  # Ensure this is present



    

# Create your views here.
