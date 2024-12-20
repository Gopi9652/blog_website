from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'));
    image=models.ImageField(upload_to='img/', blank=True, null=True)
    title=models.CharField(max_length=256)
    #slug=models.SlugField(max_length=256,unique_for_date='publish',unique=True, blank=True)
    author=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'), self.publish.strftime('%d'), self.title,self.author.username])