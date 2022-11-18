# import requests as req
# from model_utils.managers import InheritanceManager
#
#
# class Adcombo:
#
#     API_URL = 'https://api.adcombo.com/api/v2/order/create/'
#     API_KEY = 'fbf7c3d2bc305607e25b2fb5cde9394f'    #vlad API fbf7c3d2bc305607e25b2fb5cde9394f
#
#     def __init__(self):
#         self.offer_id = '33681'
#         self.base_url = 'https://land1.abxyz.info/'
#         self.price = '140'
#         self.country_code = 'PE'
#
#
#     def send_lead(self, name,phone):
#         data = {
#             'api_key': self.API_KEY,
#             'name': name,
#             'phone': phone,
#             'offer_id': self.offer_id,
#             'country_code': self.country_code,
#             'price': self.price,
#             'base_url': self.base_url,
#             'ip': '178.120.56.134',
#             'referrer': 'facebook.com',
#             'subacc': 'sub1',
#             'subacc2': 'sub2',
#             'subacc3': '',
#             'subacc4': '',
#             'utm_campaign': '',
#             'utm_content': '',
#             'utm_medium': '',
#             'utm_source': '',
#             'utm_term': '',
#             'clickid': 'sub1'
#         }
#         res = req.get(self.API_URL, params=data)
#         print(res.status_code)
#         print(res.text)
#         print(res.json())
#
# adcombo = Adcombo()
# adcombo.send_lead('test', '+1111111')


# import requests as req
# import collections
# from urllib import request, parse
#
#
#
# class LeadRockOffer:
#     KEY = '21842'
#     SECRET = '8KuDVZKiwBfWXSQGKH1Is5Hw78WN0eeV'
#     API_URL = 'https://leadrock.com/api/v2/lead/save'
#
#     # flow_url = 'https://leadrock.com/URL-64A47-9EC8B'
#
#
#     def send_lead(self):
#         data = {
#         'flow_url': 'https://leadrock.com/URL-B5D19-6F13B',
#         'user_phone': '+11111112',
#         'user_name': 'Pyhton urllib',
#         'other': '',
#         'ip': '178.120.56.134',
#         'ua': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#         'api_key': self.KEY,
#         'sign': self.SECRET,
#         'sub1': '',
#         'sub2': '',
#         'other[address]': '',
#         'other[city]': '',
#         'other[zipcode]': '',
#         'other[quantity]': '1',
#         'ajax': 1,
#         }
#         res = req.get(self.API_URL, params=data)
#         print(res)
#         print(res.status_code)
#         print(res.text)
#         print(res.json())
#
#
#
# lead_rock = LeadRockOffer()
# lead_rock.send_lead()


import requests as req

class KmaOffer:

    API_KEY = 'T5Ug9l_5gStBTeg6mUCUSQ25hjAZbRjO'  #vlas API KEY T5Ug9l_5gStBTeg6mUCUSQ25hjAZbRjO
    API_URL = 'https://api.kma.biz/lead/add'

    REFERER = 'Referer: https://facobook.com/'
    HEADERS = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }


    def __init__(self):
        self.channel = 'IgH5HI'
        self.country = 'AZ'


    def send_lead(self, name, phone,ip):
        data = {
            'channel': self.channel,
            'name': name,
            'phone': phone,
            'ip': ip,
            'country': self.country,
            'referer': self.REFERER,
            'token': self.API_KEY,
        }
        res = req.post(self.API_URL, data=data, headers=self.HEADERS)
        print(res.status_code)
        print(res.text)
        print(res.json())


kma = KmaOffer()
kma.send_lead('test', '+111111111', '178.120.56.134')
