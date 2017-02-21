# coding: utf-8

def city_country(city_name, country):

	full_name = '"' + city_name + ', ' + country + '"'

	return full_name.title()


shanghai = city_country('shanghai', 'china')
wuhan = city_country('wuhan', 'china')
guilin = city_country('guilin', 'china')
print(shanghai)
print wuhan
print guilin
