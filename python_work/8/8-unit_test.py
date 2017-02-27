# coding: utf-8

import prinnting_functions as pf

# def get_formatted_name(first_name, middle_name, last_name):

#     full_name = first_name + ' ' + middle_name + ' ' + last_name

#     return full_name.title()

# musician = get_formatted_name('x', 'd', 'h')
# print musician

# def get_formatted_name(first_name, last_name, middle_name=''):

# 	if middle_name:
# 		full_name = first_name + ' ' + middle_name + ' ' + last_name

# 	else:
# 		full_name = first_name + ' ' + last_name

# 	return full_name.title()

# musician = get_formatted_name('xxx', 'ddd', 'hhh')
# print musician

# musician = get_formatted_name('xxx', 'hhh')
# print musician

#########################################################
# def greet_users(names):

#     for name in names:
#         print("Hello!" + ' ' + name.title())

# usernames = ['tony', 'yahana', 'while']
# greet_users(usernames)

##########################################################
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models =[]

# while unprinted_designs:
# 	current_models = unprinted_designs.pop()

# 	print("Printing model:" + current_models)
# 	completed_models.append(current_models)

# print('\nThe following models have been printed')
# for completed_model in completed_models:
# 	print completed_model
#

##########################################################
# def print_models(unprinted_designs, completed_models):
# 	""" 打印模型的过程 """
#         while unprinted_designs:
#             current_models = unprinted_designs.pop()

#             print("Printing model:" + current_models)
#             completed_models.append(current_models)


# def show_completeds(completed_models):
# 	""" 显示打印设计完的模型 """
#         print('\nThe following models have been printed')
#         for completed_model in completed_models:
#             print completed_model


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # print_models(unprinted_designs, completed_models)
# # 创建副本, 不修改原来的列表
# print_models(unprinted_designs[:], completed_models)
# show_completeds(completed_models)

# print unprinted_designs

################################################################
# def make_pizza(*toppings):
# 	print(toppings)

# make_pizza('qingjiao')
# make_pizza('qingjiaog', 'putao', 'apple')

################################################################
# def make_pizza(*toppings):
# 	print("\nMaking a pizza with the following toppings:")

# 	for topping in toppings:
# 	    print("- " + topping)

# make_pizza('qingjiao')
# make_pizza('qingjiaog', 'putao', 'apple')

################################################################
# def make_pizza(size, *toppings):
# 	print("\nMaking a " + str(size) +
# 		" pizza with the following toppings:")

# 	for topping in toppings:
# 	    print("- " + topping)

# make_pizza(15, 'qingjiao')
# make_pizza(22, 'qingjiaog', 'putao', 'apple')

################################################################
# def build_profile(first, last, **user_info):
# 	profile = {}
# 	profile['first_name'] = first
# 	profile['last_name'] = last

# 	for key, value in user_info.items():
# 		profile[key] = value

# 	return profile

# xd_info = build_profile('x', 'd', city='wuhan', age=20, work='dog')

# print(xd_info)

###############################################################
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
# 创建副本, 不修改原来的列表
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completeds(completed_models)

print unprinted_designs
print completed_models
