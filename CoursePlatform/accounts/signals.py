from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile when a new user is created
    :param sender: User model
    :param instance: new user instance
    :param created: if a user is created (bool)
    :param kwargs:
    :return:
    """
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
