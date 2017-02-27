# coding: utf-8
# restaurant.py


class Restaurant(object):

    """描述一个餐馆"""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\n餐厅名称是: " + self.restaurant_name.title())
        print("菜品是: " + self.cuisine_type)

    def open_restaurant(self):
        print("餐厅正在营业中")


# make_restaurant = Restaurant('食天下', "川菜")
# make_restaurant.describe_restaurant()
# make_restaurant.open_restaurant()


# hubeicai = Restaurant('sky_food', '湖北菜')
# hubeicai.describe_restaurant()

#################################################################
class User(object):

    """docstring for User"""

    def __init__(self, first_name, last_name, **args):
        """初始化用户的基本属性"""

        self.first_name = first_name
        self.last_name = last_name
        self.args = args

    def describe_user(self):
        """返回描述性的信息"""
        full_name = self.first_name + self.last_name
        return ("姓名: " + full_name.title() + str(self.args))

    def greet_user(self):

        full_name = self.first_name + self.last_name
        print("Hello! " + full_name.title() + '\n')

bali = User('ba', 'li', age=12, city='shanghai')
sunshine = User('x', 'd')

print(bali.describe_user())
bali.greet_user()

print(sunshine.describe_user())
sunshine.greet_user()
