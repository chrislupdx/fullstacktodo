from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=25),
	body = models.TextField(null=True, blank=True),

def __str__(self):
    return self.title
