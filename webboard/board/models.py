from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # author=models.Foreignkey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    age=models.IntegerField(default=0)
    created_date=models.DateTimeField(
        default=timezone.now
    )
    published_data=models.DateTimeField(
        blank=True, null=True
    )
    
    def publish(self):
        self.published_data=timezone.now()
        self.save

    def __str__(self):
        return self.title
