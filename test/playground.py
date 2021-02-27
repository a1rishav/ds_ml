import numpy as np
n = 4
arr =np.array( [[0 , 1],  [1,  0]])
print(np.tile(arr, (n // 2, n //2)))