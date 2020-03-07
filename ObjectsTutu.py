"""
Date: 07-03-2020
Author: Goutham R(Druffl3)
Notes: Related to OOPS
"""

class circle(object):
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

class rectangle(object):
    def __init__(self,height,width,color):
        self.height = height
        self.width = width
        self.color = color

RedCircle = circle(2,"red")
BlueRectangle = rectangle(5,6,"blue")

print(RedCircle)
print(BlueRectangle)
