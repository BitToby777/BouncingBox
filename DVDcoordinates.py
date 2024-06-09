#Toby Nov 22 2023
#This is a simulation of the famous DVD Logo screen, but it allows you to pick all of its settings

import pygame

def change_angle():
    global x_value_move
    global y_value_move
    global angle
    if (angle < 91):
        angle_move = angle
    if (angle > 90):
        if (angle > 180):
            if (angle < 270):
                angle_move = angle - 180
            else:
                angle_move = 360 - angle
        else:
            angle_move = 180 - angle
    x_value_move = (angle_move / 90) * speed
    y_value_move = ((90 - angle_move) / 90) * speed
    if (angle < 91):
        y_value_move = y_value_move * -1 
    if (angle > 180):
        if (angle < 270):
            x_value_move = x_value_move * -1
        else:
            x_value_move = x_value_move * -1
            y_value_move = y_value_move * -1

box_size = 50
screen_height = int(input("What is the height of the screen? "))
screen_width = int(input("What is the width of the screen? "))
x_value = int(input("What is the starting x value? "))
y_value = int(input("What is the starting y value? "))
angle = int(input("What is the angle that your square is going in? "))
speed = int(input("What is the speed of the square? "))
box_size = 50
dis = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
x_value_move = 0
y_value_move = 0
angle_move = 0
change_angle()
while True:
    pygame.draw.rect(dis, "red", pygame.Rect(x_value, y_value, box_size, box_size))
    pygame.display.flip()
    clock.tick(30)
    if (x_value > screen_width - box_size):
        angle = 360 - angle
#        print (angle)
        change_angle()
    if (x_value < 0):
        angle = 360 - angle
#        print (angle)
        change_angle()
    if (y_value < 0):
        if (angle < 180):
            angle = 180 - angle
        else:
            angle = 540 - angle 
#        print (angle)
        change_angle()
    if (y_value > screen_height - box_size):
        if (angle < 180):
            angle = 180 - angle
        else:
            angle = 540 - angle 
#        print (angle)
        change_angle()
    dis.fill((0, 0, 0))
    x_value = x_value + x_value_move
    y_value = y_value + y_value_move
