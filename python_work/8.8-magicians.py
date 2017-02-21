# coding: utf-8

def show_magicians(magician_names):
	for name in magician_names:
		print name

def make_great(the_great, magicians):
	while magicians:
		great_magician = 'the great ' + magicians.pop()
		the_great.append(great_magician.title())


magicians = ['tony', 'yahan', 'kubu']
the_great_magicians = []


make_great(the_great_magicians, magicians[:])
show_magicians(the_great_magicians)
show_magicians(magicians)
