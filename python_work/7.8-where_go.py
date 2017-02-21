# coding: utf-8
places = {}

places_active = True

while places_active:
	name = raw_input("\nWhat's your name: ")
	place = raw_input("if you could visit one place in the world, where would you go?: ")

	places[name] = place
	repeat = raw_input("还要继续参加调查吗?输入 yes/no: ")

	if repeat == 'no':
		places_active = False

print "\n-----poll results-----"
for name, place in places.items():
	print ("%s 喜欢去的地方是 %s" % (name, place))