from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    # author=models.Foreignkey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=1)
    created_date=models.DateTimeField(
        default=timezone.now
    )
    published_data=models.DateTimeField(
        blank=True, null=True
    )


    def __str__(self):
        return self.name
