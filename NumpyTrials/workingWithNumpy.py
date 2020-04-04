"""
This script introduces to a basic usage of Numpy
Date: 4April_2020
Author: Goutham R
Notes:
pip3 install --user numpy
"""
import numpy as np

#x,y
uVector = [0,1]
vVector = [1,0]
yV = np.array([1,2])
xV = np.array([2,3])

ab = np.array([2,1,3,4])

x = np.array([0, np.pi / 2, np.pi]) # radians
y = np.sin(x) # radians

def addVector(u, v):
    '''
    Vector addition without numpy
    '''
    res = []
    for i,j in zip(u, v):
        res.append(i+j)

    return res

def addVectorWithNumpy(u: np.ndarray,v: np.ndarray) -> np.ndarray:
    '''
    Vector additiong with numpy
    '''
    res = u + v
    return res

def subVectorWithNumpy(u: np.ndarray,v: np.ndarray) -> np.ndarray:
    '''
    Vector subtraction with numpy
    '''
    res = u - v
    return res


#print(addVector(uVector, vVector))
# print("Vector addition: ", addVectorWithNumpy(np.array(uVector), np.array(vVector)))
# print("Vector subtraction: ", subVectorWithNumpy(np.array(uVector), np.array(vVector)))
# print("VectorxScalar: ", yV*2)
# print("Hadamard product: ", np.array(uVector) * yV)
# print("Dot product: ", np.dot(yV,xV))
# print("Broadcast: ", xV + 1)
# print("AB: ", ab)
# print("Mean/average of ab: ", ab.mean())
# print("Max of ab: ", ab.max())
print("Pi: ", np.pi)
print("X: ", x)
print("Y(sin(x)): ",y)
