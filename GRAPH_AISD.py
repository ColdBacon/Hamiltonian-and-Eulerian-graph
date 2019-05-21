import random

matrix = []
n=10
g=50
ilosc_wierzcholkow={}
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)
for i in range(n - 1):
    matrix[i][i+1]=1
    matrix[i + 1][i] = 1

matrix[0][n - 1] = 1
matrix[n - 1][0] = 1
MAXedge = int(n * (n - 1) * (g / 100) / 2)
edge = n

while edge < MAXedge:
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    z = random.randint(0, n - 1)
    if z == x or x == y or z == y or matrix[x][y] == 1 or matrix[x][z] == 1 or matrix[y][z] == 1:
        continue
    else:
        matrix[x][y] = 1
        matrix[y][x] = 1
        matrix[x][z] = 1
        matrix[z][x] = 1
        matrix[z][y] = 1
        matrix[y][z] = 1
        edge += 3

print ("PRAWIE DONE: ")
for i in range(n):
    print (matrix[i])
for i in range(n):
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    if x != y:
        matrix[x], matrix[y] = matrix[y], matrix[x]
        for i in range(n):
            matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]

print ("WYMIESZANA: ")
for i in range(n):
    print (matrix[i])

#nasycenie
def saturation(dict):
    sum_degree=0
    n=len(dict.items())
    for x in dict.values():
        sum_degree=sum_degree+x
    satur = sum_degree/(n*(n-1))
    return satur

#sprawdzanie czy wszystkie wierzcholki maja stopien parzysty
def parz(dict):
    for x,y in dict.items():
        if y%2==1:
            return False
    return True

#sprawdzanie spojnosci grafu
def spojnosc(dict):
    for x,y in dict.items():
        if y==0:
            return False
    return True

#slownik ze stopniami wierzcholkow
for i in range(n):
    e=0
    for j in range(n):
        e=e+matrix[i][j]
    ilosc_wierzcholkow[i]=e

print (ilosc_wierzcholkow)
print (saturation(ilosc_wierzcholkow))
print (parz(ilosc_wierzcholkow))
print(spojnosc(ilosc_wierzcholkow))

def make_connection(matrix, x, y):
    matrix[x][y] = 1
    matrix[y][x] = 1

def del_connection(matrix, x, y):
    matrix[x][y] = 0
    matrix[y][x] = 0

MATRIX = [
[0,1,1,0,0,0],
[1,0,1,1,1,0],
[1,1,0,1,1,0],
[0,1,1,0,1,1],
[0,1,1,1,0,1],
[0,0,0,1,1,0],
]

#*******************************************
#ROBI OK, ALE USUWA MACIERZ
def Hamilton(matrix,v,V,result):
    V.append(v)
    for w in range(len(matrix[v])):
        if matrix[v][w] == 1 and w not in V:
            del_connection(matrix, v, w)
            result = Hamilton(matrix, w, V, result)
            if result:
                return result
    if len(V) == len(matrix) and matrix[v][0] == 1:
        return V+[0]
    else:
        V.pop()
        if len(V) > 1:
            last = V[-1]
            make_connection(matrix, v, last)
#print (Hamilton(matrix,0,[],[]))

RESULT=[]
def multiHamilton(matrix,v,V,RESULT):
    if len(V)==len(matrix) and matrix[v][0]:
        RESULT.append(V+[0])
    if not len(V):
        V.append(0)
    for w in range(len(matrix[v])):
        if matrix[v][w] and w not in V:
            V.append(w)
            multiHamilton(matrix,w,V,RESULT)
            V.pop()

print ("WIELE HAMILTONÓW")
multiHamilton(matrix,0,[],RESULT)
print(RESULT)

def Euler(matrix, sv):
        out = []
        stack = [sv]
        while stack:
            v = stack[-1]
            is_edge = 0
            for i in range(len(matrix)):
                if matrix[v][i] == 1:
                    matrix[v][i] = -1
                    matrix[i][v] = -1
                    stack.append(i)
                    is_edge = 1
                    break
            if is_edge == 1:
                continue
            stack.pop()
            out.append(v)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]*=-1
        return out
print ("EULER")
print(Euler(MATRIX,0))
