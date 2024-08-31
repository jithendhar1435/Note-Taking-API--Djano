from django.urls import path
from .views import CreateNoteView, FetchNoteView, QueryNotesView, UpdateNoteView

urlpatterns = [
    path('notes/', CreateNoteView.as_view(), name='create_note'),
    path('notes/<int:pk>/', FetchNoteView.as_view(), name='fetch_note'),
    path('notes/query/', QueryNotesView.as_view(), name='query_notes'),
    path('notes/<int:pk>/', UpdateNoteView.as_view(), name='update_note'),
]
