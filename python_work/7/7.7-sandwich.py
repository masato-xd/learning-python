sandwich_orders = ['sucai', 'shuiguo', 'huotui', 'pastrami', 'pastrami', 'pastrami', 'pastrami']
finished_sanwiches = []

# while sandwich_orders:
# 	current_sandwich = sandwich_orders.pop()
# 	print "I made your %s sandwich" % current_sandwich

# 	finished_sanwiches.append(current_sandwich)
# print "\nall sandwich"
# for i in finished_sanwiches:
# 	print i

print "sorry everyone, no pastrami"

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print "I made your %s sandwich" % current_sandwich

	finished_sanwiches.append(current_sandwich)
print "\nall sandwich"
for i in finished_sanwiches:
	print i