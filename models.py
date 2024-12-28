from django.db import models

# Create your models here.

class women(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]
