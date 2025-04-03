import pyautogui
import numpy as np
import math

#sets the center of the circel (in this case)
x_center = 1920/2 -400
y_center = 1080/2

#sets the radius of the circle that you wnat to draw
#sets the delta in degrees that you wnat (how many sides will the circel have) 
#sets the starting angle
radius = 100
delta = 90
deg = 0

#moves the mouse to the position where it will start drawing
pyautogui.moveTo(x_center + radius, y_center)

#draws the lines until you have a complete circle
while deg <=360:
    pyautogui.dragTo(math.cos(deg*math.pi/180)*radius + x_center, math.sin(deg*math.pi/180)*radius + y_center, button='left', duration=0.0, _pause = False)
    deg += delta
