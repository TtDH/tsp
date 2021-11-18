import numpy as np

def calcCost(data, route):
    total_cost = 0
    for i in range(len(route)):
        idx = 0 if i+1==len(route) else i+1
        total_cost += np.linalg.norm(data[route[idx]] - data[route[i]])
    return total_cost

def shapingData(filename):
    # "~~.tsp"を扱いやすい形式に変える関数
    # ~~(dir)
    #   raw
    #   data
    #   route
    f = open("./data.txt")
    while True :
        line = f.readline()
        if not line:
            break
        words = line.replace(':', '').split()
        if words[0] == 'DIMENSION':
            datalen = int(words[1])
        elif words[0] == 'NODE_COORD_SECTION':
            break

    data = np.zeros((datalen, 2))
    for i in range(datalen):
        sp = f.readline().split()
        data[i,0] = sp[1]
        data[i,1] = sp[2]
    f.close()
    print(f"length:{datalen}")
    print(f"data:\n{data}")

    return data, datalen

def getData(dirname):
    f = open('/root/prj/data/' + dirname + '/data.txt')
    lines = f.readlines()
    datalen = len(lines)
    data = np.zeros((datalen, 2))
    for i in range(datalen):
        sp = lines[i].split()
        data[i, 0] = sp[1]
        data[i, 1] = sp[2]
    f.close()

    f = open('/root/prj/data/' + dirname + '/route.txt')
    lines = f.readlines()
    route = np.zeros(datalen, dtype=int)
    for i in range(datalen):
        # routeの添え字は 1 ~ len なので
        # 0 ~ len-1 に調整する
        route[i] = int(lines[i])-1
    f.close()

    return datalen, data, route
    
datalen, data, route = getData('berlin52')
# print(datalen)
# print(data)
# print(route)
print(calcCost(data, route))