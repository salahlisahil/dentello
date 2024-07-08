from django.db import models


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return f'<PostImage {self.image}>'


class Post(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    images = models.ManyToManyField(PostImage)

    def __str__(self):
        return f'<Post {self.title}>'
