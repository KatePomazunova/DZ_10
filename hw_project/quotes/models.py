from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    date_born = models.CharField(max_length=50)
    location_born = models.CharField(max_length=150)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
