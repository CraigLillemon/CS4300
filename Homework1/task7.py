import numpy as num
#can now use an array from numpy
array = num.array([1, 2, 3, 4,5])
#this array follows all the rule of matricies of math, which means it adds subtracts multiplys and dicides in occurdance to math rules
#since this array is adding a [1][4] + [1][1] it will auto convert it to be a [1][4] array for the sum
array += 1
print(array )

assert array[0] == 2
assert array[1] == 3
#the following code wont work in comparion to numpy
#testArray = [1, 2, 3, 4, 5]
#testArray += 1
#print(testArray)