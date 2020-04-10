"""
This script introduces to 2D Array using Numpy.
Date: 10April_2020
Author: Goutham R
Notes:
pip3 install --user numpy
pip3 install --user matplotlib
"""
import numpy as np
import matplotlib.pyplot as plot

# a = [[11,12,13],[21,22,23],[31,32,33]]
# A = np.array(a) #Creates a 3x3 Matrix

# print(A)
# print("Number of lists nested in the 2Darray/matrix: ", A.ndim)
# print("Shape of the matrix: ",A.shape) # returns a tuple of rowxcolumn -> 3x3
# print("Size of the 2Darray/Matrix: ", A.size)
# print(type(A.shape))
# print("2Darray/Matrix slicingA[0,0:2]: ", A[0,0:2]) # A[row,column] returns a ndarray.
# print("2Darray/Matrix slicingA[0:2,2]: ", A[0:2,2]) # A[row,column] returns a ndarray.
# print("2Darray/Matrix slicingA[0:2,0:2]: ", A[0:2,0:2])

# x = np.array([[1,0],[0,1]])
# y = np.array([[2,1],[1,2]])
# print("X:\n",x)
# print("Y:\n",y)
# print("Matrix addition(X + Y): \n", x + y )
# print("Scalar product(Y.2): \n", y*2)
# print("Hadamard product(X.Y):\n",x * y)

vA = np.array([[0,1,1],[1,0,1]])
vB = np.array([[1,1],[1,1],[-1,1]])
vZ = np.dot(vA,vB)

print("A matrix: \n",vA, "\nShape of A: ",vA.shape)
print("\nB matrix: \n",vB, "\nShape of B: ",vB.shape)
print("Matrix product(dot product) of A x B: \n", vZ, "\nShape of Z: ",vZ.shape)
