
alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
new_points = alien_0['points']
# print 'you just earned ' + str(new_points) + " points!"
# print alien_0['color']
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# print alien_0
alien_0['color'] = 'yellow'
# print alien_0['color']
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
elif alien_0['speed'] == 'fast':
	x_increment = 3

alien_0['x_position'] += x_increment
#print 'new x: %s' % alien_0['x_position']
print alien_0
del alien_0['points']