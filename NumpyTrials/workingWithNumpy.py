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

#resultant vector
zVector = []

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
print("Vector addition: ", addVectorWithNumpy(np.array(uVector), np.array(vVector)))
print("Vector subtraction: ", subVectorWithNumpy(np.array(uVector), np.array(vVector)))
