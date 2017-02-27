aliens = []

for i in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10
	elif alien['color'] == 'yellow':
			alien['color'] = 'red'
			alien['speed'] == 'fast'
			alien['point'] = 15			

for alien in aliens[:5]:
	print alien
print '...'