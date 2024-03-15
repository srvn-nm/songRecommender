from django.db import models

class Request(models.Model):
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('failure', 'Failure'), ('ready', 'Ready'), ('done', 'Done')], default='pending')
    song_id = models.CharField(max_length=255, blank=True, null=True)
