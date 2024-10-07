import uuid
from django.db import models
from django.core.exceptions import ValidationError
from .mindmap import MindMap

class Node(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4().hex[:50], editable=False)
    title = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    mind_map = models.ForeignKey(MindMap, on_delete=models.CASCADE, related_name='nodes')
    created_at = models.DateTimeField(auto_now_add=True)
    flow_data = models.JSONField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id', 'parent', 'mind_map']),
        ]

    def __str__(self):
        return self.title

    def clean(self):
        if self.parent and self.parent.id == self.id:
            raise ValidationError("A node cannot be its own parent.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

