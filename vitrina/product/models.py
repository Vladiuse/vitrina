from django.db import models

# Create your models here.


class Offer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название оффера', unique=True)
    desc = models.TextField(blank=True, verbose_name='Описание оффера')
    price = models.CharField(max_length=20, blank=True, verbose_name='Цена оффера + валюта')
    image = models.ImageField(blank=True, verbose_name='картинка оффера', upload_to='offers')
    activa = models.BooleanField(blank=True, default=False, verbose_name='Опубликован')


    def __str__(self):
        return str(self.name)

