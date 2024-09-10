from django.db import models

class Article(models.Model):
    title = models.CharField('Title', max_length=20)
    anons = models.CharField('Anons', max_length=40)
    full_text = models.TextField('Full Text')
    date = models.DateTimeField('DateTime')

    def __str__(self):
        return self.title
# Create your models here.
