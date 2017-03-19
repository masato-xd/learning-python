# try:
#     print(5 / 0)
# except ZeroDivisionError as e:
#     print(e)
#     print("you can't division by zero")


print("Give me two Nu. and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = raw_input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = raw_input("Second number: ")
    if second_num == 'q':
        break

# 错误处理代码块
# try：可能出错的代码
# except：给出指定的异常返回提醒
# else：try成功以后需要执行的代码
    try:
        answer = int(first_num) / int(second_num)
    except:
        print("you can't division by zero")
    else:
        print(answer)
