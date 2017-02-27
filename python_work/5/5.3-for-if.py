# users = ['admin', 'jack', 'xd', 'aby', 'masato']
# users = []

# if users:
# 	for user in users:
# 		if user == 'admin':
# 			print "Hello admin, would you like to see a status report?"
# 			#print 1

# 		else:
# 			print "\tHello %s, thank you for logging in again" % user
# else:
# 	print "We need to find some users"

current_users = ['aAa', 'bbB', 'ccc', 'ddd', 'Eee']
new_users = ['zzz', 'bbb', 'ccC', 'yyy', 'aaa']

current_users_lowers = []
for current_user in current_users:
	current_users_lowers.append(current_user.lower())

for new_user in new_users:
	if new_user.lower() in current_users_lowers:
		print "change name"
	else:
		print 'this name ok'