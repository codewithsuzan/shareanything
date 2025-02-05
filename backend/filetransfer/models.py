from django.db import models
import uuid
from datetime import timedelta
from django.utils.timezone import now

class SharedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='uploads/')
    pin = models.CharField(max_length=8)  # Store PIN
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return now() > self.created_at + timedelta(hours=1)
