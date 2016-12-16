# coding: utf-8

# alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
# new_points = alien_0['points']
# # print 'you just earned ' + str(new_points) + " points!"
# # print alien_0['color']
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# # print alien_0
# alien_0['color'] = 'yellow'
# # print alien_0['color']
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# elif alien_0['speed'] == 'fast':
#     x_increment = 3

# alien_0['x_position'] += x_increment
# # print 'new x: %s' % alien_0['x_position']
# print alien_0
# del alien_0['points']

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'xudeng': 'python'
}

# 默认遍历所有的键
# favorite_languages == favorite_languages.keys()
# for key in favorite_languages.keys():
# 	print "%s like language %s" % \
# 		(key.title(), favorite_languages[key].title())

# sorted() 对key 做排序
# for key in sorted(favorite_languages.keys()):
# 	print "%s like language %s" % \
# 		(key.title(), favorite_languages[key].title())

# set 去重
# for value in set(favorite_languages.values()):
# 	print value

names = ['xudeng', 'zsh']

for name in names:
	if name not in favorite_languages.keys():
		print name
		print 'welcome into our as?'
	else:
		print name
		print 'thank you !'