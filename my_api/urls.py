from django.urls import path
from .views import CreateNote,UpdateNote

urlpatterns=[
    path('', CreateNote.as_view(),name='create_note'),
    path('<int:pk>/',UpdateNote.as_view(), name='update_note')
]