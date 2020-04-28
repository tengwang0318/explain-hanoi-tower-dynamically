import turtle
import random


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


# parameter k is used to confirm one pale's location
def drawpole_1(k, my_turtle):
    color_map = ['red', 'green', 'yellow']
    my_turtle.up()
    my_turtle.pensize(10)
    my_turtle.speed(0)  # fastest
    my_turtle.goto(500 * (k - 1), 100)
    my_turtle.down()
    my_turtle.color(color_map[k])
    my_turtle.goto(500 * (k - 1), -100)
    my_turtle.goto(500 * (k - 1) + 30, -100)
    my_turtle.goto(500 * (k - 1) - 30, -100)


def drawpole_3():  # draw three poles
    my_turtle = turtle.Turtle()

    drawpole_1(0, my_turtle)
    drawpole_1(1, my_turtle)
    drawpole_1(2, my_turtle)


def pole_stack():  # create poles's Stack()
    poles_stack = []
    for i in range(3):
        poles_stack.append(Stack())

    return poles_stack


def creat_plates(n):  # draw n plates
    plates = []
    for i in range(n):
        plates.append(turtle.Turtle())
    color_map = ['red', 'blue', 'green', 'yellow', 'pink']
    for i in range(n):
        plates[i].up()
        plates[i].color(color_map[random.randint(0, 4)])
        plates[i].shape("square")
        plates[i].shapesize(1, 10 - i)
        plates[i].goto(-500, -90 + 30 * i)

    return plates


# move this plate from original place to new place
def move_disk(plates, poles_stack, first_place, final_place):
    loc = poles_stack[first_place].peek()
    plates[loc].goto((first_place - 1) * 500, 150)
    plates[loc].goto((final_place - 1) * 500, 150)
    height = poles_stack[final_place].size()
    plates[loc].goto((final_place - 1) * 500, -90 + 30 * height)


def move_tower(plates, poles_stack, height, first_pole, with_pole, final_pole):
    if height >= 1:
        move_tower(plates, poles_stack, height - 1, first_pole, final_pole, with_pole)
        move_disk(plates, poles_stack, first_pole, final_pole)
        poles_stack[final_pole].push(poles_stack[first_pole].pop())
        move_tower(plates, poles_stack, height - 1, with_pole, first_pole, final_pole)


my_win = turtle.Screen()
drawpole_3()
my_win.title("hanni tower problem!(The color about plates and poles are random.)")
count = int(input("Please enter the number of layers of the hanni tower:"))
plates = creat_plates(count)
poles = pole_stack()
for i in range(count):
    poles[0].push(i)
move_tower(plates, poles, count, 0, 1, 2)
my_win.exitonclick()
