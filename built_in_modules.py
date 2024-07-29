import os
from statistics import *
#(* means to import every function in that file)

import math
#Using the OS to create a folder
#os.mkdir('folder_create_test')
#os.rmdir('folder_create_test')
print(os.getcwd())



ages = [23, 24, 56, 47, 88, 90]

print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

print(math.pi)
print(math.sqrt)
print(math.pow(10, 2))