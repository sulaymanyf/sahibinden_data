import json

import requests

headers = {
    'Host': 'api.sahibinden.com',
    'X-J3PopQvX-d': 'o_0',
    'X-J3PopQvX-c': 'A10GMhNyAQAAYlcnTmVqsjhcHop-0qeYEmP1uB729Vj3fPWK_DmElFl4d-f5Abw5H6yfQNuyFooO8YLqosIO8Q==',
    'X-NewRelic-ID': 'VQACUF9bCBAGXVNbAQQOUVc=',
    'x-client-profile': 'Generic_v2.1',
    'x-timestamp': '1589460298776',
    'X-J3PopQvX-b': '-vv6jqv',
    'X-J3PopQvX-a': 'eK3il=GWpwsv0lU4KpG5uYw2Tn0D84s76qfK-CVIAwRp5aX6-Ggbi2TlX4HrBoj6RCYF8NTrWcFf7KvQyNnkjYDZuqjIjHwphSbinQ0We58rdp5sU19iGdCaZAnOLclrKDKCgsHisM0OB--Uf_LPjG4dwIQNanDC1H-lIw0nDPy49WyKVBbGCCno2R5g2Vzck=jkYaT8ecn15T5WqCPZg2ReLHg0yPs2Cb9EjVUfb4V-AM16VZTL1lBV_JtSHtXcnD-KciQ05EGGpjgws_MRwYrCV5KIWnh93GUcrsdzQrKR2EfZOa7CUeM1-=WOL7-G4qeezoiLbTr6rjzfRYQYNWXbKpBb9c6wVHVM-KlP4ydbOq8zmm8VuJ3kWyHvfCM-ItPt1PJvqhJdo=yQtdiaAVHBI_lEY3fo7Osy_e2H23qcqY-ei0RmRt8YtD3XB1VlBLQVRisdiI6YZfaVvcEuB9oJAhLaTHnF=esMMrmgzrf2svwQPKlAaEn_uXZSYPyeBpJYufct5v8ggMz68rnggrX7_acjBRf4VThlV87DB7yWGk7VWyBG7k7RpBzkWrUUkS_whuLP7lRnL62-cSnLP_=BNU1XSF_OesPr_zwC7JZQh0HPVj_DITNaRN6CqfH7JVWsXbA4v_c4NdkVJt21=XYeKYC2ZER3gQRCbOQJL_yI7ie-DInRZV2Asy8XODZ4IED25FGbkvsuSCY3s5=S4OHG-mf3sN=pS0peiRD0BUIWRAPAFsXlgMdNPaKjO5v4DOLIDw8cK9zu2R7hSNvhlYoaCh2Sv5YFfSjGQaQXQpU4tlfv7aXdPCQQh2D9MqkOIzU7XyYiFdGgijLLjgK3k3jDPkwA-l0tX3ng__533C6WCTb5BKJb41-S_z_wNTAdIuIDIEq7SK9Xk2DhL_ODYfuvT0=e8=Notf3r-ARFMXs6ZnDORiTB0=0KumWp8dCa0TrBBsyGwby0=-l3oDALYDyvphWO8sKYR78NJ9C-wpRK_XbyF2C7i=5gGEQMuRmD9aRnA_DHallWm-sT_DDnHMLysPwVWR=9WC9WoOMFJ-fdnBKcL-yTFBbjUvroJavotbZEMXrvk=rkVL1RJKSvMEYZQ4Sq0DHl-pZnpZvPgPDSifKwD=vGniwIQtFyF1rid2=I4svWumO6kFsyP8K7Z1wjuUFJu1l5MInJqPNkncWsw4MT=K6m9aQC07fcw9iZsAXDHa10um5gWpabr0TNo_Ma_B=VQ3APttKbn9IC4Sdco_e_v-UhpYNqX5secypX16MYn31Z4b8kybwAXXfN35RPdkIoXQo_3S=9WdVP8ApEQK9HS4pg9AmiShBKUj8CcJYnq1-oL4euSPslbnRq37qyGZBhayggaB8HlVrp9qFENHd8pVlFVGLEQbnCqzsNuMWqTgjuDKlp=aoMUEs66gBdPdqVkOWHp7nvH7=ZydERGT4GSS-hbjG5IivLK6zDzwXykXsI3bdPDbJmhf=e3LmaWIf7Cq1FGhypUiiGE1EEp-t5Sz2Ye4863SpA0sn667zR-t7qEXlaZa9Cj9Pysi',
    'User-Agent': 'Sahibinden-IOS/4.7.0(2020/05/12,iPhone XR,iOS13.4.1)v3',
    'x-api-hash': '990D982B88D72A54A4AC3B043F6071B175562753',
    'X-Device-Id': 'A5C12204690A4E40B603E0EBFCDC1B47',
    'X-J3PopQvX-z': 'p',
    'x-bundle-id': 'com.sahibinden.sahibinden',
    'x-app-version': '4.7.0',
    'x-language': 'tr',
    'Accept-Language': 'en-us',
    'X-J3PopQvX-f': 'Aw8KNhNyAQAA37fE7fHlDN7CVbcQKayUVKq6tbbEdhDB-ndr1skD7N95htl1AToXMlmfQDXk7xUO8YLqosIO8Q==',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-J3PopQvX-e': 'a;0BxKOBIobbfLYW4YIG7LYnwZjhAwxDus5PrdSRuih8BF65S8w7X_-vMNVwJmztw7YQtBiMEO7G8aXq8htlkucQzt8iJMZblK5kwKvqMT0i1tM-DCz4Mc1Kno6IndjjoT7P_OtEXuRjkRjtumtn5ilK0D9dr7e5YJUrFf2KamyChBqmLTQ0d5UJyxO8osKq5it9hdSTVNoZ_gIhYP77AJk7xGF1BIaDL1YOygUhQkZuL_6bNDMM-x0H0Ig6LrgNoyzFg6lQ7ubFam3oByuCT3f7Hd3MCpwiODDt0GNW2Y5rU5IiUp0C6pkagZL7Te2Ut2HIkf0ULrpktWTu179q8dMN4fim379pmgY7WnjQJZMiAReKAe2PAZSiFosK3Qsxs0N5Vp1-7wq56HnoZFFrUOu59XLAa9Npo94VPRamXcJSQELFrfTavW0h1QklyfS6FpwLP-X4zovtlQ_M7HyGlXEXUjr7Zhq5kfZ6zYD1b9dXtx2kRKfS58QzBGkI9RO5db99H18k4JOVf0jy4boD59Tyf36ZCremDW_ql5ZhFo_pLkSxXHu2jN9o1nu8j4gwva_X8Cat0lmUmkpmcgKbT0E9DahqtxCFXZ_loLO1amnlfIzl9fMZU7ENZcWXMewGAGSXtsVhqTnY02P9aL-1Vr1AwBdL74DGLamt9vsaTC5lQjsZp_35bHIw4qQPYSF3LSBUA04y9LDQLzYXK0243GFcZS_FBNCEYPi_bR2oMPd1wbgdHMo2jzlcuGpqfZnv7ahj0lyI2GJ8mwSlouPDcvTgL2HDE=;3eDt8LcQ1TIUWWqCg5pZMtRwWJkQEQprVfgW5bNyeDc=',
    'x-api-key': 'f51c6d9290ea9522aceac00f3b87a0002695d38a',
    'idfa': 'CBB40715-EE01-4985-982E-925C09A4416E',
}

params = (
    ('a811', ['40597', '40599', '40594', '62364', '40600', '40595', '62365', '40598', '40593', '40601', '40596', '62366']),
    ('a812', ['40604', '40728', '40602', '40603', '40605', '40606']),
    ('price_currency', '1'),
    ('category', '16633'),
    ('price_max', '1500000'),
    ('address_quarter', ['51395', '23114', '51399', '52036', '51400', '23097']),
    ('sorting', 'price_desc'),
    ('m:searchMeta', 'true'),
    ('m:includeCategoryTree', 'false'),
    ('m:includeMatchingFavoriteClassifieds', 'true'),
    ('m:smartTextSearch', 'true'),
    ('pagingOffset', '0'),
    ('pagingSize', '200'),
    ('language', 'tr'),
)

response = requests.get('https://api.sahibinden.com/sahibinden-ral/rest/classifieds/search', headers=headers, params=params)

# print(response.json())
json_dicts=json.dumps(response.text)
print(response.json())
print(type(response.json()['response']['classifieds']))
print(len(response.json()['response']['classifieds']))
print(json.dumps(response.json()['response']['classifieds'],indent=4))
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.sahibinden.com/sahibinden-ral/rest/classifieds/search?a811=40597&a812=40604&price_currency=1&category=16633&price_max=1500000&a812=40728&a812=40602&a812=40603&a812=40605&a812=40606&a811=40599&a811=40594&a811=62364&a811=40600&a811=40595&a811=62365&a811=40598&a811=40593&a811=40601&a811=40596&a811=62366&address_quarter=51395&address_quarter=23114&address_quarter=51399&address_quarter=52036&address_quarter=51400&address_quarter=23097&sorting=price_desc&m%3AsearchMeta=true&m%3AincludeCategoryTree=false&m%3AincludeMatchingFavoriteClassifieds=true&m%3AsmartTextSearch=true&pagingOffset=0&pagingSize=20&language=tr', headers=headers)
