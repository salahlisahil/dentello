from django.db import models


class Comment(models.Model):
    fullname = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Comment {self.fullname}>'
