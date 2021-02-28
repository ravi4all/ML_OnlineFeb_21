Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x = np.array([4,3,5,7,8,4,2,3,7,8])
>>> np.delete(x, 3)
array([4, 3, 5, 8, 4, 2, 3, 7, 8])
>>> np.delete(x, [1,5])
array([4, 5, 7, 8, 2, 3, 7, 8])
>>> x = np.array([[4,3,5],[7,8,4],[2,3,8]])
>>> np.delete(x, 0)
array([3, 5, 7, 8, 4, 2, 3, 8])
>>> x = np.array([[4,3,5],[7,8,4],[2,3,8]], axis=0)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x = np.array([[4,3,5],[7,8,4],[2,3,8]], axis=0)
TypeError: 'axis' is an invalid keyword argument for array()
>>> np.delete(x, 0, axis=0)
array([[7, 8, 4],
       [2, 3, 8]])
>>> x
array([[4, 3, 5],
       [7, 8, 4],
       [2, 3, 8]])
>>> np.delete(x, 0, axis=0)
array([[7, 8, 4],
       [2, 3, 8]])
>>> np.delete(x, 0, axis=1)
array([[3, 5],
       [8, 4],
       [3, 8]])
>>> np.delete(x, 2)
array([4, 3, 7, 8, 4, 2, 3, 8])
>>> x
array([[4, 3, 5],
       [7, 8, 4],
       [2, 3, 8]])
>>> np.delete(x, 1,1)
array([[4, 5],
       [7, 4],
       [2, 8]])
>>> np.delete(x, 1,0)
array([[4, 3, 5],
       [2, 3, 8]])
>>> x = np.array([4,3,5,7,8,4,2,3,7,8])
>>> x
array([4, 3, 5, 7, 8, 4, 2, 3, 7, 8])
>>> np.where(x == 7)
(array([3, 8], dtype=int64),)
>>> np.delete(x, np.where(x == 7))
array([4, 3, 5, 8, 4, 2, 3, 8])
>>> 