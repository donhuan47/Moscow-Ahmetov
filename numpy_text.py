import numpy as np

dataScientist = [130, 132, 137]
productManager = [127, 140, 137]
designer = [118, 118, 127]

emploees = np.array([dataScientist, productManager, designer])
emploees[0, ::2] = emploees[0, ::2] * 1.1
print(emploees.dtype)

np.nonzero()

# print(a[:, 2])  # [ 2  6 10 14]
# print(a[1, :])  # [4 5 6 7]
# print(a[1, ::2])  # [4 6]
# print(a[:, :-1])
# print(a[:-2])
