from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        ordering = ['-published_date']

    def get_absolute_url(self):
        return reverse('post_details', kwargs = {"pk": self.pk})

    def __str__(self):
        return self.title
