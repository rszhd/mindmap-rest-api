from django.db import models
from django.contrib.auth.models import User

class MindMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=200)
    flow_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return self.title