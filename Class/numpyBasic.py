import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2 * np.pi,1000)
y = np.sin(x)

plt.plot(x,y)
plt.show()


#
# pythonArr = [[1, 2, 4], [3, 8, 10], 6]
# numpyArr = np.array(pythonArr)
#
#
#
#
# # print(pythonArr[1][2])
# # print(type(numpyArr))
# print(np.zeros([3,4]))
#
#
#
#
# a = np.array([[2,4], [3,4], [7,4]])
# b = np.array([2,4,1,3,2,3]).reshape(2,3)
#
# print(a)
# print(b)
# # print(b-a) : error (ValueError: operands could not be broadcast together with shapes (2,3) (2,2) )
# print (a @ b)
# # print (a * b) : ValueError
