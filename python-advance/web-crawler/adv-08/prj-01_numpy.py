import numpy as np
listA=[7,89,30,-7,29,3,20,74,33,8]
index=np.argsort(listA)
print(index)
print(np.array(listA)[index])