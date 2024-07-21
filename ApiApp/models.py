from django.db import models

# Create your models here.


class Tasks(models.Model):
    Task_title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    # author = models.CharField()
    Task = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return self.Task_title
