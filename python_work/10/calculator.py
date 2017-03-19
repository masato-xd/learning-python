# -*- coding: utf-8 -*-


issue = 'tell me two Num. we can sum this:\n'
issue += "Enter 'q' exit"
print(issue)

while True:
    num_a = raw_input("first Num: ")
    if num_a == 'q':
        break

    num_b = raw_input("second Num: ")
    if num_b == 'q':
        break

    try:
        answer = int(num_a) + int(num_b)
    except ValueError as e:
        print("don't zhuanhuan str")
    else:
        print(answer)
