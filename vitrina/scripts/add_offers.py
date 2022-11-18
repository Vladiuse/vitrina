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
    image_no_space_name = i.replace(' ', '_')
    img_full_path = os.path.join(PATH, i)
    img_name = os.path.splitext(i)[0]
    price = f'{r.randint(10, 80) * 10}$'
    new_image = shutil.copy(img_full_path, os.path.join(PATH_TO_SAVE_IMAGE, image_no_space_name))
    offer = Offer()
    offer.name = img_name
    offer.desc = LOREM
    offer.price = price
    offer.image = os.path.join('offers', image_no_space_name)
    print(os.path.join('media', image_no_space_name))
    offer.activa = True
    offer.save()


