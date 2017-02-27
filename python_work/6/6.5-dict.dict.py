users = {
	'xdeng': {
		'first': 'xu',
		'last': 'deng',
		'age': 18
	},
	'xhang': {
		'first': 'xu',
		'last': 'hanh',
		'age': 22
	}
}

for user, user_info in users.items():
	print ("UserName:" + user)
	fullname = user_info['first'] + user_info['last']
	age = user_info['age']

	print ("\tFullName:" + str(fullname))
	print ("\tAge: " + str(age))
