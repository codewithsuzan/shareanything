from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import now
from .models import SharedFile
import random

@api_view(['POST'])
def upload_file(request):
    """ Upload a file with a random PIN """
    file = request.FILES['file']
    pin = str(random.randint(100000, 999999))
    shared_file = SharedFile.objects.create(file=file, pin=pin)
    return Response({'pin': pin, 'file_id': str(shared_file.id)})

@api_view(['POST'])
def retrieve_file(request):
    """ Retrieve file if PIN matches within 1 hour """
    pin = request.data.get('pin')
    file = SharedFile.objects.filter(pin=pin).first()

    if not file:
        return Response({'error': 'Invalid PIN'}, status=400)

    if file.is_expired():
        file.delete()
        return Response({'error': 'File expired'}, status=400)

    return Response({'file_url': file.file.url})
