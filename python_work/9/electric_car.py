# coding: utf-8

from car import Car
from car import Battery

class ElectricCar(Car):

    """docstring for ElectricCar"""

    def __init__(self, make, model, year):
        """初始化父类的属性, 在初始化电动车特有的属性"""
        super(ElectricCar, self).__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery(71) # 创建一个Battery()类的实例作为属性

    # def describe_battery(self):
    #     """打印一条描述电瓶容量的信息"""
    #     print("This car has a " + str(self.battery_size) + "-KWH battery.")

    def fill_gas_tank(self):
    	""""重写父类方法"""
    	print("doesn't need a gas tank!")

if __name__ == '__main__':

	# my_tesla = ElectricCar('tesla', 'model-s', 2016)

	# print(my_tesla.get_descriptive_name())
	# my_tesla.describe_battery()

	# my_tesla.update_odomter(25)
	# my_tesla.read_odomter()

	# my_tesla.fill_gas_tank()

	my_tesla = ElectricCar('tesla', 'model-s', 2017)
	print(my_tesla.get_descriptive_name())
	my_tesla.battery.get_range()