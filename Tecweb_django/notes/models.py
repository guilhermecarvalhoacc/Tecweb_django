from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id}.{self.title}"
        

