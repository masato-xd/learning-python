# -*- coding: utf-8 -*-
import turtle


def draw_triangle(some_turtle):
    for x in xrange(0, 3):
        some_turtle.forward(50)
        some_turtle.right(120)
    # some_turtle.speed(0)

if __name__ == '__main__':

    window = turtle.Screen()

    benji = turtle.Turtle()
    benji.shape("turtle")
    benji.speed(1)

    # x
    benji.right(120)
    benji.forward(100)

    benji.pu()
    x = benji.setx(5)
    benji.pd()

    benji.right(120)
    benji.forward(100)

    # D
    benji.pu()
    benji.seth(270)
    benji.setx(55)
    benji.pd()

    benji.forward(100)
    benji.left(90)
    benji.circle(50, 180)

    window.exitonclick()
    # 旋转360度就是一个圆, 36次*10度
    # for x in xrange(1, 37):
    #     benji.speed(0)
    #     draw_triangle(benji)
    #     benji.right(10)

    # window.exitonclick()
