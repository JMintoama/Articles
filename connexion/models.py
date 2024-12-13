from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    desc=models.TextField()
    image = models.ImageField(upload_to='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
