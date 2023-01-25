from django.db import models

# Create your models here.
class category(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
          return self.name
class article(models.Model):
  Title = models.CharField(max_length=100)
  Text = models.TextField()
  category = models.ForeignKey(category, on_delete=models.CASCADE)
