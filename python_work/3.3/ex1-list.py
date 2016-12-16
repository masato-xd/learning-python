#address = ['ruishi', 'tokoyo', 'xila', 'wanwan', 'yidali']
#print address
#
#address_sotred = sorted(address)
#print address_sotred
#
#print address
#
#address.reverse()
#print address
#address.reverse()
#print address
#
#address.sort()
#print address
#address.sort(reverse=True)
#print address
#print len(address)
#
#for i in range(10):
#	print i
#print i

# list_b = [i   for i in xrange(1, 10001)]
# list_a = list(range(1, 11))
# list_c = [i for i in range(3, 31) if i % 3 == 0]
# list_d = [i ** 3 for i in range(1, 11)]
#list_f = list_a[:]
#print list_a
#print list_f
#list_a.pop()
#print list_a
#print list_f

string_a = ' The first three items in the list are:'
string_b = 'the last three items in the list are:'
list_a = list(string_a.split())
list_b = list(string_b.split())
for a in list_a:

	print "%s in a" % a

for b in list_b:
	print "%s in b" % b
#print string_b
#print string_a
