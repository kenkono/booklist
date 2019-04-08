from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Impression(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    impression = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pictures', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.impression


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    favorite = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

