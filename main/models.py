from django.db import models

class Like(models.Model):
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

