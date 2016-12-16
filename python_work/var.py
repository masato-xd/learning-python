# -*- coding: utf-8 -*-
# Filename : var.py

number = 23
running = True

while running:
    guess = int(raw_input('输入一个数字:'))

    if guess == number:
        print "恭喜你 答对了"
        running = False

    elif guess < number:
        print "再大一点"

    else:
        print "在小一点"

else:
    print "循环结束"

print 'Done'