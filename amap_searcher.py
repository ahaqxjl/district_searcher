#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import json
import requests

from models import District


# TODO read host and key from configuration file
url = 'http://restapi.amap.com/v3/config/district'
key = 'ef5655ca17a2c9d6adf67810b12cf9c1'


def search_all_district():
    # get all province
    # TODO 将查询和处理分开
    params = {'key': key, 'subdistrict': 3}
    print('=====start searching======')
    r = requests.get(url, params=params)
    print('=====search result========')
    print(r.text)
    with open('amap_result.json', 'w') as result:
        result.write(json.dumps(r.json(), indent=4, ensure_ascii=False))

    # get cities
    # get disctrict


def parse_search_result():
    with open('amap_result.json', 'r') as result:
        r_json=json.load(result)
    provinces = []
    cities = []
    districts = []
    # 第一层是国家
    if 'status' in r_json and r_json['status'] == '1' and 'districts' in r_json and 'districts' in r_json['districts'][0]:
        print('=====convert result to model=====')
        for province_json in r_json['districts'][0]['districts']:
            province = District(province_json, None)
            provinces.append(province)
            # print('=====district=====')
            # province.print()
            for city_json in province_json['districts']:
                city = District(city_json, province)
                cities.append(city)

                for district_json in city_json['districts']:
                    district = District(district_json, city)
                    districts.append(district)

        sql = ''
        for province in provinces:
            # province.print()
            sql += province.generate_insert_sql() + '\n'

        for city in cities:
            sql += city.generate_insert_sql() + '\n'

        for district in districts:
            sql += district.generate_insert_sql() + '\n'

        with open('result.sql', 'w') as result:
            result.write(sql)
            # if (province.city_code == '010'):
                # count = 0
                # for city_json in province_json['districts'][0]['districts']:
                    # count += 1
                    # city = District(city_json, None)
                    # print("INSERT INTO E_CITY (ID, NAME, PROVINCE_ID) VALUES(E_CITY_SEQ.nextval, '%s', 1);" % (city.name))
                # print(count)

            # if (province.city_code == '022'):
                # count = 0
                # for city_json in province_json['districts'][0]['districts']:
                    # count += 1
                    # city = District(city_json, None)
                    # print("INSERT INTO E_CITY (ID, NAME, PROVINCE_ID) VALUES(E_CITY_SEQ.nextval, '%s', 4);" % (city.name))
                # print(count)

            # if (province.city_code == '021'):
                # count = 0
                # for city_json in province_json['districts'][0]['districts']:
                    # count += 1
                    # city = District(city_json, None)
                    # print("INSERT INTO E_CITY (ID, NAME, PROVINCE_ID) VALUES(E_CITY_SEQ.nextval, '%s', 11);" % (city.name))
                # print(count)

            # if (province.city_code == '023'):
                # count = 0
                # for city_json in province_json['districts'][0]['districts']:
                    # count += 1
                    # city = District(city_json, None)
                    # print("INSERT INTO E_CITY (ID, NAME, PROVINCE_ID) VALUES(E_CITY_SEQ.nextval, '%s', 24);" % (city.name))
                # for city_json in province_json['districts'][1]['districts']:
                    # count += 1
                    # city = District(city_json, None)
                    # print("INSERT INTO E_CITY (ID, NAME, PROVINCE_ID) VALUES(E_CITY_SEQ.nextval, '%s', 24);" % (city.name))
                # print(count)

# search_all_district()
parse_search_result()
