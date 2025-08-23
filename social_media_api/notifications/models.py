from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'notifications')
    actor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'actions')
    verb = models.CharField(max_length = 250)
    is_read = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)
    # Generic relation to any model
    target_content_type = models.ForeignKey(ContentType, null = True, blank = True, on_delete = models.SET_NULL)
    target_object_id = models.PositiveIntegerField(null = True, blank = True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
