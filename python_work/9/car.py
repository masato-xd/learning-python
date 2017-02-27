# coding: utf-8
# car.py


class Car(object):

    """docstring for Car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        log_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return log_name.title()

    def read_odomter(self):
        print("This car has " + str(self.odometer_reading) + ' miles on it.')

    def update_odomter(self, mileage):
        """将值设置为指定的值
                禁止将值回调, 变小"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def incremetn_odomter(self, mileage):
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        print('This car has 50L gas tank')


class Battery(object):

    """模拟电动汽车电瓶"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size))

    def get_range(self):
        if self.battery_size <= 70:
            range = 240
        elif self.battery_size > 70:
            range = 320

        message = 'This car can go ' + str(range)
        message += ' miles'
        print message

if __name__ == '__main__':
    my_new_car = Car('bmw', 'x1', 2017)

    print(my_new_car.get_descriptive_name())
    my_new_car.read_odomter()
    # 直接修属性的值
    my_new_car.odometer_reading = 23
    my_new_car.read_odomter()
    # 通过方法修改属性的值
    my_new_car.update_odomter(50)
    my_new_car.read_odomter()
    # 通过方法递增
    my_new_car.incremetn_odomter(100)
    my_new_car.read_odomter()
