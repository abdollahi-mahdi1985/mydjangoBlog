from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='defualt.jpg', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "...."
