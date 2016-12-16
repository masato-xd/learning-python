# coding: utf-8
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities
print '-' * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']


# do it by using the state then cities dict
# 密歇根州有(has)底特律
print '-' * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]


# print every state abbreviation
# 打印每个州的缩写
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# 打印每个州包含的城市
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)


# now do both at the same time
# 打印每个州, 州缩写, 州包含的城市
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbrevi %s and has city %s"  % (
		state, abbrev, cities[abbrev])

# 安全的获取可能不存在的key
print '-' * 10
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."


# 获取具有默认值的城市

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city