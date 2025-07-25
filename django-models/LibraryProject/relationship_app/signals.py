from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def crate_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
