import pandas as pd
import numpy as np

# numpy.array(object, dtype = None, copy = True, order = 'K', subok = False, ndmin = 0)
dt1 = [1, 2, 3, 4, 5, '6']
arr1 = np.array(dt1,subok= False)
print (arr1)
print (arr1[0].dtype())