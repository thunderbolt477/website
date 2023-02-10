from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    post = models.CharField(max_length=9000)

    def __str__(self):
        return f"User posted {self.title} with content {self.post}"