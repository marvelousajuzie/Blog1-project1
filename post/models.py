from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length =100)
    body = models.CharField(max_length = 20000)
    created_at = models.DateTimeField(default = datetime.now)

def __str__(self):
    self.title
    