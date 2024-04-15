from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from online_book_shop.accounts.models import Profile, BookShopUser


@receiver(post_save, sender=BookShopUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
