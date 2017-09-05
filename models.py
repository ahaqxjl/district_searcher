# _*_ coding: utf-8 _*_


class District(object):

    def __init__(self, city_code, ad_code, name, center, level):
        self.city_code = city_code
        self.ad_code = ad_code
        self.name = name
        self.center = center
        self.level = level
        self.parent = parent

    def __init__(self, district_json, parent):
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
        self.parent = parent

    def print(self):
        print('city_code: ', self.city_code)
        print('ad_code: ', self.ad_code)
        print('name: ', self.name)
        print('center: ', self.center)
        print('level: ', self.level)
        print('parent', self.parent)

    def generate_insert_sql(self):
        table_name = 'district'
        city_code = 'city_code'
        ad_code = 'ad_code'
        name = 'name'
        center = 'center'
        level = 'level'
        parent = 'parent'
        parent_value = 'null'
        if self.parent is not None:
            parent_value = "id from {} where {} = '{}'".format(table_name, ad_code, self.parent.ad_code)
        format_str = "insert into {} ({}, {}, {}, {}, {}) select '{}', '{}', '{}', '{}', {};"
        return format_str.format(table_name, city_code, ad_code, name, level, parent, self.city_code, self.ad_code, self.name, self.level, parent_value)

    def __str__(self):
        return self.name

