from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    title  = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    contents = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created    = models.DateTimeField(auto_now_add=True)
    changed    = models.DateTimeField(auto_now=True)
    status     = models.CharField(max_length=10,
                                  choices=STATUS,
                                  default='rascunho')


    def __str__(self):
        return self.title





# Create your models here.
