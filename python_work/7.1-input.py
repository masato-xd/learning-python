# coding: utf-8
#name = raw_input("please enter your name:")

# print("Hello, " + name + "!")
#prompt = 'if you tell us who you are, we can you see.'
#prompt += '\nWhat is your name?'

# name = raw_input(prompt)
# print '\n' + name

#number = raw_input('please tell me , u how many people eat?: ')
#number = int(number)

#if number > 8:
#    print "sorry, can't kong zhuozi"
#else:
#    print "ok, welcome for u"

#number_a = raw_input('tell me some number: ')
#number_a = int(number)

#if number_a % 2 == 0:
#    print 'this number is even'
#else:
#    print 'this number is odd'

###########################################

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' when you are finished."
message = ""

active = True
#while message != 'quit':
#    message = raw_input(prompt)
#    #print(message)   
#    if message != 'quit':
#        print message
#while active:
    
#    message = raw_input(prompt)
#    if message == 'quit':
#        break           # break退出循环
        #active = False # 修改标志active
#    else:
#        print(message)

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue
    print current_number
