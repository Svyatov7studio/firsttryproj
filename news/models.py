from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    textpost = models.TextField()
    date = models.DateTimeField()
#    image =

    def __str__(self):
        return self.title
