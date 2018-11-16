from django.db import models

class Base(models.Model):
    # general
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
