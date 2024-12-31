from django.db import models
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=women.Status.PUBLISHED)
        
        

class women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT= 0, 'Черновик'
        PUBLISHED = 1, 'Опублековано'
    
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255,unique=True, db_index=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices,default=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]
        
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
