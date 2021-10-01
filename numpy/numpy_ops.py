import numpy as np

'''
Numpy arrays are :
    - of same data type
    - faster than lists
    - use precompiled C code and use multiple cores
    - On 2 numpy arrays of equal size we can do element wise mathematical operation
        - This operation is much faster than list with lambda
        - Eg. multiplying in multiplying 2 matrix, operations are done independent to
              each other <------ vectorized operation 
    
    np.ones(): Create an array of 1s
    np.zeros(): Create an array of 0s
    np.random.random(): Create an array of random numbers between 0 and 1
    np.arange(): Create an array with increments of a fixed step size
    np.linspace(): Create an array of fixed length        
        
        
'''


list_3 = [1, 2, 3]

# declaring
print(np.array([list_3]))

# Full
array_x = np.full((5, 4), 100, dtype=int)
print("Full : {}".format(array_x))

#arange
print("\narange\n")
print(np.arange(0, 12, 2))

# reshape
print("\nreshape\n")
print(np.array(np.random.rand(12, 1), dtype=float).reshape(2, 6))
# let numpy figure out
print(np.array(np.random.rand(12, 1), dtype=float).reshape(2, -1))

# transpose
print("\ntranspose\n")
print(array_x.T)

#stacking
# Horizontal stack --> number of rows must be same
# Vertical stack --> number of colums must be same

print("\n vertical stacking\n")
array_1 = np.arange(12).reshape(3, 4)
array_2 = np.arange(8).reshape(2, 4)
print(array_1)
print(array_2)
print(np.vstack((array_1, array_2)))

# vectorize custom function

print("\n vectorize\n")
func = np.vectorize(lambda x : x/5)
print(func(array_1))

# dot product

print("\n dot product\n")
a = np.array([3,4,5])
b = np.array([1,3,5])
print (np.dot(a,b))

# shearing

print("\n shearing\n")
S = np.matrix([[1,1], [0,1]])

# Declare the vectors that define the corners of the rectangle.

a = np.matrix([[0],[0]])
b = np.matrix([[2],[0]])
c = np.matrix([[2],[1]])
d = np.matrix([[0],[1]])

a_sheared = S * a
b_sheared = S * b
c_sheared = S * c
d_sheared = S * d

# cos inverse
print("\n cos inverse\n")
vector_a = np.array([1  ,1,0,0])
vector_b = np.array([1,1,1,0])
cosine_angle = np.arccos(np.dot(vector_a, vector_b) /
               (np.linalg.norm(vector_a) * np.linalg.norm(vector_b)))
print(cosine_angle)

# determinant
print("\n determinant\n")
A = np.array([[2, 3], [-1, 4] ])
np.linalg.det(A)

A = np.array([[2, -1, -1],
              [2, -1, 1],
              [4, -2, 3]])
print("Determinant : {}".format(np.linalg.det(A)))

# system of three equations
A = np.array([[1, 5, -1],
              [2, 3, -2],
              [-3, 4, 0]])
b = np.array([1, 2, 0])

# compute the inverse
A_inv = np.linalg.inv(A)

# solution: A_inv * b
x = np.dot(A_inv, b)
print(x) # returns [ 0.  0.]

print("\n Rank \n")
A = np.array([[2, -1, -1],
              [2, -1, 1],
              [4, -2, 3]])
print(np.linalg.matrix_rank(A))

print("\n eigenvalues and eigen vectors \n")
A = np.array([[2, 0],
              [0, 3]])

# c is the array of eigenvalues
# v is the matrix with eigenvectors as the columns
c, v = np.linalg.eig(A)
print("Eigenvalues : \n {}".format(c))
print("Eigenvectors : \n {}".format(v))

