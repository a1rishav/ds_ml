from functools import reduce

'''
Lambda :
x= lambda input : output
'''

# lamda func :
greater = lambda a, b : a if a > b else b
print("Lambda : {}".format(greater(10, 20)))

'''
Map :
map(lambda func , iterable) 
'''
cube = list(map(lambda x : x**3, [1, 2, 3]))
print("Map : {}".format(cube))

'''
Filter :
filter(lambda func , iterable) 
'''
list_answer = list(filter(lambda x : x % 5 ==0, [2,3,5,7,10,12,15]))
print("Filter : {}".format(list_answer))

'''
Reduce :
reduce(lambda func, iterable)
'''
reduce_out = reduce(lambda x,y : x + " : " + y, ["hi", "there", "this", "is", "a", "test" ])
print("Reduce output : {}".format(reduce_out))

'''
Comprehension
'''
product_list = [ i*j for i in range(1, 3) for j in range(1, 4) ]
print("Comprehension : {}".format(product_list))