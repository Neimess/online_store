from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=False)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")

    def __str__(self):
        return f"User: {self.user}"

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
