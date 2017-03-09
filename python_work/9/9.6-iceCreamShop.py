# coding: utf-8
# iceCreamShop.py


class Restaurant(object):

    """描述一个餐馆"""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\n餐厅名称是: " + self.restaurant_name.title())
        print("菜品是: " + self.cuisine_type)

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, new_number):
        self.number_served += new_number

    def read_number(self):
        print("就餐人数: " + str(self.number_served))

    def open_restaurant(self):
        print("餐厅正在营业中")


class IceCreamStand(Restaurant):

    """docstring for IceCreamStand"""

    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple', 'orange', 'caomei', 'banana', 'chocolate']

    def show_flavors(self):
        print("冰激凌有以下口味: ")
        for flavor in self.flavors:
            print("- " + flavor)


if __name__ == '__main__':
    my_ice_cream = IceCreamStand('冰天下', '冰激凌')
    my_ice_cream.show_flavors()
    my_ice_cream.read_number()
    my_ice_cream.open_restaurant()
    my_ice_cream.describe_restaurant()
