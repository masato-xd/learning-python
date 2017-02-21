# coding: utf-8
# make_car.py


def make_car(automaker, car_model, **car_infos):
    print("\n接下来要生产的汽车信息如下")

    car = {}
    car['automaker'] = automaker.title()
    car['car_infos'] = car_model.title()
    for key, value in car_infos.items():
        car[key] = value

    return car
