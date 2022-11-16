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


class Lead(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50,verbose_name='Имя клиента')
    phone = models.CharField(max_length=15, verbose_name='Номер клиента')
    ip = models.GenericIPAddressField(blank=True, verbose_name='Ip аддресс пользователя', null=True)
    datetime = models.DateTimeField(auto_now_add=True)



