from django.db import models

class Article(models.Model):
    title = models.CharField('Title', max_length=25, default='Default Title')
    anons = models.CharField('Anons', max_length=100, default='Default Anons')
    full_text = models.TextField('Full Text',  default='Default Full Text')
    date = models.DateTimeField('DateTime')

    def __str__(self):
        return self.title
# Create your models here.
