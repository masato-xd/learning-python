# -*- coding: utf-8 -*-
import turtle


def draw_square(some_turtle):
    for i in xrange(0, 4):
        some_turtle.forward(100)  # 向前100距离
        some_turtle.right(90)  # 向右90度


def draw_triangle(some_turtle):
    for i in xrange(0, 3):
        some_turtle.forward(100)
        some_turtle.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")  # 创建窗口(画布)

    brad = turtle.Turtle()
    brad.color("red")  # 颜色
    brad.shape("turtle")  # 形状

    draw_square(brad)

    shally = turtle.Turtle()
    shally.shape("classic")
    shally.color("blue")
    shally.circle(100)  # 圆

    benji = turtle.Turtle()
    benji.color("green")

    draw_triangle(benji)

    window.exitonclick()  # 点击关闭窗口


draw_art()
