from django.urls import path
from .views import upload_file, retrieve_file

urlpatterns = [
    path('upload/', upload_file, name='upload-file'),
    path('retrieve/', retrieve_file, name='retrieve-file'),
]
