"""
Date: 07-03-2020
Author: Goutham R(Druffl3)
Notes: Related to OOPS
"""

class circle(object):
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

    def addRadius(self,newRadius):
        self.radius = self.radius + newRadius

class rectangle(object):
    def __init__(self,height,width,color):
        self.height = height
        self.width = width
        self.color = color

    def _privateMethod(self):
        pass

RedCircle = circle(2,"red")
BlueRectangle = rectangle(5,6,"blue")

print(RedCircle.radius)
RedCircle.addRadius(12)
print(RedCircle.radius)
print(dir(BlueRectangle))
