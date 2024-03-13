from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.title
    
