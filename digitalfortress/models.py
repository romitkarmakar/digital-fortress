from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user =models.OneToOneField(User, on_delete = models.CASCADE)
    score = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Round(models.Model):
    round = models.IntegerField()
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)

class Hint(models.Model):
    hint = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    position = models.CharField(max_length=100)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)

    def __str__(self):
        return self.hint

class Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hint = models.ForeignKey(Hint, on_delete=models.CASCADE)