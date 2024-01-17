from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = (
    ('not_started', 'Not Started'),
    ('in_progress', 'In Progress'),
    ('reviewing', 'Reviewing'),
    ('on_hold', 'On Hold'),
    ('completed', 'Completed')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    status = models.CharField(
        max_length=11,
        choices=STATUS,
        default=STATUS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

