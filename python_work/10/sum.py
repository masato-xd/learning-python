issue = 'tell me two Num. we can sum this:\n'
print(issue)

num_a = raw_input("first Num: ")
num_b = raw_input("last Num: ")

try:
    answer = int(num_a) + int(num_b)
except ValueError as e:
    print("don't zhuanhuan str")
else:
    print(answer)
