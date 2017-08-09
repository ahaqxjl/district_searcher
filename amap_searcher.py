#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import requests

from models import District


# TODO read host and key from configuration file
url = 'http://restapi.amap.com/v3/config/district'
key = 'ef5655ca17a2c9d6adf67810b12cf9c1'


def search_all_district():
    # get all province
    params = {'key': key}
    print('=====start searching======')
    r = requests.get(url, params=params)
    print('=====search result========')
    print(r.text)
    with open('country_result.json', 'w') as result:
        result.write(r.text)

    r_json = r.json()
    if 'status' in r_json and r_json['status'] == '1' and 'districts' in r_json and 'districts' in r_json['districts'][0]:
        print('=====convert result to model=====')
        for province_json in r_json['districts'][0]['districts']:
            province = District(province_json)
            print('=====district=====')
            province.print()

    # get cities
    # get disctrict
    pass


search_all_district()
