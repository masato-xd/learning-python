# coding: utf-8

#ten_things = "Apples Oranges Crows Telephone Light Sugar"
#
#stuff = ten_things.split(' ')
#
# more_stuff = ["Day", "Night", "Song",
#              "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#    stuff.append(more_stuff.pop())
#
#    print len(stuff)

# for i in more_stuff:
#    if len(stuff) != 10:
#        stuff.append(i)
#
# print stuff
#
#
# def all_the_args(*args, **kw):
#    print args
#    print kw
#
#li = [1, 2, 3, 4]
#a = 'fdafda'
#dict_a = {'a': 1, 'b': 2}
#
#all_the_args(a, *li, **dict_a)

# 函数嵌套函数


# def creat_adder(x):
#    def adder(y):
#        return x + y
#    return adder
# 将函数赋值给一个变量
#adder = creat_adder(10)
# print adder(3)


class Human(object):

    # 类属性, 所有实例/对象都具有
    species = "H. sapines"

    # 构造方法, 初始化属性
    def __init__(self, name):
        self.name = name
        self.age = 10

    # 实例方法
    def say(self, msg):
        return '%s: %s' % (self.name, msg)

    # 类方法会被所有实例共享
    # 类方法在调用时，会将类本身作为第一个函数传入
    # 类方法不能访问实例变量, 可以访问类变量
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法在调用时，不会传入类或实例的引用
    # 不能访问实例变量
    @staticmethod
    def grunt():
        return '*grunt*'


i = Human('Ian')
j = Human('Jole')

print i.age
print i.say('hi')
print j.say('hello')
print Human.grunt()

Human.species = 'i change this is'


