#!/usr/bin/python
#coding: utf-8

'''ab is a'ddress, b'ook'''

ab = {  'abc':'abc@123.com',
        'def':'def@456.com',
        'Larry':'larry@mail.org',
        'Spammer':'spammer@mail.org'
        }

print "abc's address is %s" % ab['abc']

ab['Guido'] = 'guido@mail.org'

del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)


for name, address in ab.items():
    print '%s at %s' % (name, address)

if 'Guido' in ab:
    print "\nGuido's address is %s" % ab['Guido']
