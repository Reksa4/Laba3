from turtle import *
from math import *

shape('turtle')


def zero():
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    penup()
    right(90)
    forward(300)
    pendown()



def one():
    penup()
    right(90)
    forward(100)
    left(90)
    pendown()
    left(45)
    forward(sqrt(2) * 100)
    right(135)
    forward(200)
    penup()
    left(90)
    forward(100)
    left(90)
    forward(200)
    right(90)
    pendown()



def two():
    forward(100)
    right(90)
    forward(100)
    right(45)
    forward(sqrt(2) * 100)
    left(135)
    forward(100)
    penup()
    forward(100)
    left(90)
    forward(200)
    right(90)
    pendown()


def three():
    forward(100)
    right(135)
    forward(sqrt(2) * 100)
    left(135)
    forward(100)
    right(135)
    forward(sqrt(2) * 100)
    penup()
    left(135)
    forward(200)
    left(90)
    forward(200)
    right(90)
    pendown()



def four():
    right(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    backward(200)
    penup()
    right(90)
    forward(100)
    left(90)
    forward(200)
    right(90)
    pendown()


def five():
    forward(100)
    right(180)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(180)
    forward(200)
    left(90)
    forward(200)
    right(90)
    pendown()


def six():
    penup()
    forward(100)
    pendown()
    right(135)
    forward(sqrt(2) * 100)
    left(45)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    backward(100)
    right(90)
    penup()
    forward(100)
    left(90)
    forward(200)
    right(90)
    pendown()



def seven():
    forward(100)
    right(135)
    forward(sqrt(2) * 100)
    left(45)
    forward(100)
    penup()
    left(90)
    forward(200)
    left(90)
    forward(200)
    right(90)
    pendown()

def eight():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(90)
    backward(100)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(100)
    backward(100)
    right(90)
    penup()
    forward(100)
    left(90)
    forward(200)
    right(90)
    pendown()


def nine():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    backward(100)
    right(90)
    forward(100)
    right(135)
    forward(sqrt(2) * 100)
    left(135)
    penup()
    forward(200)
    left(90)
    forward(200)
    right(90)
    pendown()

a = [2,4,0]
penup()
backward(300)
pendown()
for i in range(len(a)):
    if (a[i] == 1):
        one()
    elif (a[i] == 2):
        two()
    elif (a[i] == 3):
        three()
    elif (a[i] == 4):
        four()
    elif (a[i] == 5):
        five()
    elif(a[i] == 5):
        six()
    elif(a[i] == 7):
        seven()
    elif(a[i] == 8):
        eight()
    elif(a[i] == 9):
        nine()
    elif(a[i] == 0):
        zero()


