import os
import math

def utGetFileName(fileName): #return filename without extention
    return os.path.basename(fileName).split('.')[0]
def utRoundup(x):
    return int(math.ceil(x / 10.0)) * 10
def utCheckDir (dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)