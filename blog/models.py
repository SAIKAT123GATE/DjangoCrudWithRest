from django.db import models

# Create your models here.


class Blog(models.Model):
    artist = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
