# coding: utf-8
# import make_car
# from make_car import make_car
# from make_car import make_car as mc
# import make_car as make_c
from make_car import *

# def sanmingzhi(*toppings):

# 	print("要做的三明治有以下食材")
# 	for topping in toppings:
# 		print('- ' + topping)

# sanmingzhi('apple', 'orange', 'banana')


car = make_car('bmw', 'auto',
	color='green',
	tow_package=False)

print(car)
