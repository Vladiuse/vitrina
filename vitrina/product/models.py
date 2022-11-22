import requests as req
from django.db import models
from model_utils.managers import InheritanceManager
import os
from django.template import Template, Context, RequestContext
from django.conf import settings


# Create your models here.


class Category(models.Model):
    MINI_LANDS_DIR_NAME = 'categorys_mini_land'
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=20, verbose_name='Имя категории')
    mini_land = models.CharField(max_length=30, blank=True, verbose_name='Пусть в мини прокле оффера')

    def __str__(self):
        return str(self.name)

    def get_mini_land(self):
        path = os.path.join(f'media/{self.MINI_LANDS_DIR_NAME}/{self.mini_land}.html')
        try:
            with open(path, encoding='utf-8') as file:
                text = file.read()

            template = Template(text)
            content = {
                'product': self
            }
            context = Context(content)
            result = template.render(context)
            return str(result)
        except FileNotFoundError as error:
            return 'no find'


class PublicOffers(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(public=True)


class Offer(models.Model):
    MINI_LANDS_DIR_NAME = 'mini_lands'
    CATEGORY = [
        ('gipa', 'Гипертония'),
        ('diabet', 'Диабет'),
        ('sustavs', 'Суставы'),
    ]

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'

    objects = InheritanceManager()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Название оффера', unique=True)
    desc = models.TextField(blank=True, verbose_name='Описание оффера')
    price = models.CharField(max_length=20, blank=True, verbose_name='Цена оффера + валюта')
    image = models.ImageField(blank=True, verbose_name='картинка оффера', upload_to='offers')
    public = models.BooleanField(blank=True, default=False, verbose_name='Опубликован')

    mini_land = models.CharField(max_length=30, blank=True, verbose_name='Пусть в мини прокле оффера')

    def __str__(self):
        return f'{self.pk}:{self.name}'

    # objects = models.Manager()
    published = PublicOffers()

    def show(self):
        print('123')

    def get_mini_land(self):
        path = os.path.join(f'media/{self.MINI_LANDS_DIR_NAME}/{self.mini_land}.html')
        try:
            with open(path, encoding='utf-8') as file:
                text = file.read()

            template = Template(text)
            content = {
                'product': self
            }
            context = Context(content)
            result = template.render(context)
            return str(result)
        except FileNotFoundError as error:
            return 'no find'

    @staticmethod
    def get_next(current_offer_id):
        offers = Offer.objects.all()
        for pos, offer in enumerate(offers):
            if offer.pk == current_offer_id:
                try:
                    model = offers[pos + 1]
                except IndexError:
                    model = offers.first()
                return model.pk

    @staticmethod
    def get_prev(current_offer_id):
        offers = Offer.objects.all()
        for pos, offer in enumerate(offers):
            if offer.pk == current_offer_id:
                try:
                    model = offers[pos - 1]
                except AssertionError:
                    model = offers.last()
                return model.pk

    def send(self, lead):
        offer = Offer.objects.get_subclass(pk=self.pk)
        offer.send_lead(lead)


class AdcomboOffer(Offer):
    class Meta:
        verbose_name = 'Adcombo Оффер'
        verbose_name_plural = 'Офферы Adcombo'

    API_URL = 'https://api.adcombo.com/api/v2/order/create/'
    API_KEY = '_02ae7ffc3405c078074682b7b2abae9f'

    offer_id = models.CharField(max_length=10, verbose_name='Айди оффера в Adcombo / offer_id')
    base_url = models.URLField(verbose_name='ссылка лэнда оффера / base_url')
    # price = models.CharField(max_length=10, verbose_name='Цена оффера')
    country_code = models.CharField(max_length=10, verbose_name='Страна оффера iso / country_code')

    def send_lead(self, lead):
        data = {
            'api_key': self.API_KEY,
            'name': lead.name,
            'phone': lead.phone,
            'offer_id': self.offer_id,
            'country_code': self.country_code,
            'price': self.price,
            'base_url': self.base_url,
            'ip': lead.ip,
            'referrer': 'facebook.com',
            'subacc': 'sub1',
            'subacc2': 'sub2',
            'subacc3': '',
            'subacc4': '',
            'utm_campaign': '',
            'utm_content': '',
            'utm_medium': '',
            'utm_source': '',
            'utm_term': '',
            'clickid': 'sub1'
        }
        lead.sending_data = data
        lead.save()
        try:
            res = req.get(self.API_URL, params=data)
            lead.status_code = res.status_code
            lead.response = res.json()
            lead.save()
        except BaseException as error:
            lead.error = str(error)
            lead.save()


class LeadRockOffer(Offer):
    KEY = '20857'
    SECRET = '1cBU3EI1bn7I9zLBbjGn1JDgZMkZnoJK'
    API_URL = 'https://leadrock.com/api/v2/lead/save'

    flow_url = models.URLField()

    class Meta:
        verbose_name = 'LeadRock Оффер'
        verbose_name_plural = 'Офферы LeadRock'

    def send_lead(self, lead):
        data = {
            'flow_url': 'https://leadrock.com/URL-64A47-9EC8B',
            'user_phone': lead.phone,
            'user_name': lead.name,
            'other': '',
            'ip': lead.ip,
            'ua': '',
            'api_key': self.KEY,
            'sign': self.SECRET,
            'sub1': '',
            'sub2': '',
            'other[address]': '',
            'other[city]': '',
            'other[zipcode]': '',
            'other[quantity]': '1'
        }


class KmaOffer(Offer):
    class Meta:
        # abstract = True
        verbose_name = 'Оффер KMA'
        verbose_name_plural = 'Офферы KMA'

    API_KEY = 'T5Ug9l_5gStBTeg6mUCUSQ25hjAZbRjO'  # vlas API KEY T5Ug9l_5gStBTeg6mUCUSQ25hjAZbRjO
    API_URL = 'https://api.kma.biz/lead/add'

    REFERER = 'Referer: https://facobook.com/'
    HEADERS = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    channel = models.CharField(max_length=10, verbose_name='Номер потока')
    country = models.CharField(max_length=2, verbose_name='Страна оффера')

    def send_lead(self, lead):
        data = {
            'channel': self.channel,
            'name': lead.name,
            'phone': lead.phone,
            'ip': lead.ip,
            'country': self.country,
            'referer': self.REFERER,
            'token': self.API_KEY,
        }
        lead.sending_data = data
        lead.save()
        try:
            res = req.post(self.API_URL, data=data, headers=self.HEADERS)
            lead.status_code = res.status_code
            lead.response = res.json()
            lead.save()
        except BaseException as error:
            lead.error = str(error)
            lead.save()


class Lead(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя клиента')
    phone = models.CharField(max_length=15, verbose_name='Номер клиента')
    ip = models.GenericIPAddressField(blank=True, verbose_name='Ip аддресс пользователя', null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    status_code = models.CharField(max_length=10, blank=True, verbose_name='Статуст ответа от пп')
    sending_data = models.JSONField(blank=True, null=True, verbose_name='Отправляемые данные')
    response = models.JSONField(blank=True, null=True, verbose_name='Ответ от пп')
    error = models.TextField(blank=True, verbose_name='Текст отшибки')

    def send(self):
        offer = self.offer
        print(offer, type(offer))
        for i in dir(offer):
            print(i)
        offer.send(self)
        # self.offer.send(self)
