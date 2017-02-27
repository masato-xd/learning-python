# coding: utf-8
# eat_food_num.py


class Restaurant(object):

    """描述一个餐馆"""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\n餐厅名称是: " + self.restaurant_name.title())
        print("菜品是: " + self.cuisine_type)

    def set_number_served(self, new_number)	:
        self.number_served = new_number

    def increment_number_served(self, new_number):
        self.number_served += new_number

    def read_number(self):
        print("就餐人数: " + str(self.number_served))

    def open_restaurant(self):
        print("餐厅正在营业中")


if __name__ == '__main__':

    restaurant = Restaurant('食天下', '川菜')
    restaurant.describe_restaurant()
    restaurant.increment_number_served(70)
    restaurant.set_number_served(50)
    restaurant.read_number()
