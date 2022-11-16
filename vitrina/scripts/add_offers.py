"""
Создание позиций на базе картинок с папки store
"""

from product.models import Offer
import os
import random as r
import shutil
LOREM = 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
PATH = '/home/vlad/PycharmProjects/vitrina/store'
PATH_TO_SAVE_IMAGE = '/home/vlad/PycharmProjects/vitrina/vitrina/media/offers'

Offer.objects.all().delete()

for i in os.listdir(PATH):
    img_full_path = os.path.join(PATH, i)
    img_name = os.path.splitext(i)[0]
    price = f'{r.randint(10, 80) * 10}$'
    new_image = shutil.copy(img_full_path, os.path.join(PATH_TO_SAVE_IMAGE, i))
    offer = Offer()
    offer.name = img_name
    offer.desc = LOREM
    offer.price = price
    offer.image = os.path.join('offers', i)
    print(os.path.join('media', i))
    offer.activa = True
    offer.save()


