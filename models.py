# _*_ coding: utf-8 _*_


class District(object):

    def __init__(self, city_code, ad_code, name, center, level):
        self.city_code = city_code
        self.ad_code = ad_code
        self.name = name
        self.center = center
        self.level = level

    def __init__(self, district_json):
        if 'citycode' in district_json:
            self.city_code = district_json['citycode']
        if 'adcode' in district_json:
            self.ad_code = district_json['adcode']
        if 'name' in district_json:
            self.name = district_json['name']
        if 'center' in district_json:
            self.center = district_json['center']
        if 'level' in district_json:
            self.level = district_json['level']

    def print(self):
        print('city_code: ', self.city_code)
        print('ad_code: ', self.ad_code)
        print('name: ', self.name)
        print('center: ', self.center)
        print('level: ', self.level)

