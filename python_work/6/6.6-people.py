peoples = [
	{'xd': {'first_name': 'xu', 'last_name': 'deng',
			'age': 20, 'city': 'shanghai'}},
	{'xh': {'first_name': 'xu', 'last_name': 'hanh',
			'age': 10, 'city': 'chengdu'}},
	{'zsh': {'first_name': 'zhao', 'last_name': 'shuhong',
			'age': 18, 'city': 'shanghai'}}	
]

# for people in peoples:
# 	for name, infos in people.items():
# 		print (name.title() + " this info is:")
# 		for data in infos.keys():
# 			print "\t%s: %s" % (data, infos[data])
# print peoples[0]['xd']['first_name']


# animal

duoduo = {'name': 'duoduo', 'tpye': 'cat', 'owner': 'xudeng'}
maomao = {'name': 'maomao', 'tpye': 'dog', 'owner': 'xuhang'}
meimei = {'name': 'meimei', 'tpye': 'dog', 'owner': 'zshuhong'}
pets = [duoduo, maomao, meimei]

for pet in pets:
	print "%s :" % pet['name']
	if pet['name'] != 'name':
		for name, info in pet.items():
			print "\t%s is  %s:" % (name, pet[name]) 
