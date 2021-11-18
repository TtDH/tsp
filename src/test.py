import math
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

def getData(dataname):
    f = open(dataname)

def calcCost(data, route):
    total_cost = 0
    for i in range(len(route)):
        idx = 0 if i+1==len else i+1
        total_cost += data[route[idx]] - data[route[i]]
    return total_cost

def distance(pos):
    return np.linalg.norm(pos)

# python test.py [dataname]
if __name__ == '__main__':
    args = sys.argv
    # if len(args) != 1 :
    #     print('Argument error')
    dataname = args[0]

    data, datalen = getData(dataname)
    opt_root = getOptData(dataname)

    method = ""
    start = time.time()
    if method == "" :
        route = _search(data)
    elapsed_time = time.time() - start
    
    cost = calcCost(data, route)
    opt_cost = calcCost(data, opt_root)
    
    printResult(route, cost, opt_cost, opt_root)
    # plotRoot(route, data)