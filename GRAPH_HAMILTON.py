import random
n=20
d=0.5
matrix=[]
ilosc_wierzcholkow={}
ilosc_jedynek=(int)(n*(n-1)/2*d)

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)

for i in range(n-1):
    matrix[i][i+1]=1
    ilosc_jedynek=ilosc_jedynek-1
matrix[n-1][0]=1
ilosc_jedynek=ilosc_jedynek-1

def saturation(dict):
    sum_degree=0
    n=len(dict.items())
    for x in dict.values():
        sum_degree=sum_degree+x
    satur = sum_degree/(n*(n-1))
    return satur

while (ilosc_jedynek>0):
    i = random.randint(0,n-2)
    j = random.randint(i,n-1)

    if (matrix[i][j]==0 and i!=j):
        matrix[i][j]=1
        ilosc_jedynek=ilosc_jedynek-1

#uzupelniamy dolnatrojkatna macierz, graf nieskierowany
for i in range(n):

    for j in range(n):
        if (matrix[i][j]):
            matrix[j][i]=1

#wszystkie wierzcholki o stopniu parzystym
for k in range(n):
    for i in range(n):
        parzystosc = 0
        for j in range(n):
            if matrix[i][j]:
                parzystosc = parzystosc + 1
        if parzystosc%2==1:
            j = random.randint(0,n-1)
            while(i==j or j == i+1 or j == i-1 or (i==0 and j == n-1) or (j==0 and i == n-1)):
                j = random.randint(0,n-1)
            if matrix[i][j]==1:
                matrix[i][j]=0
                matrix[j][i]=0
            else:
                matrix[i][j]=1
                matrix[j][i]=1

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

for i in range(n):
    print (matrix[i])
print (ilosc_wierzcholkow)

print(saturation(ilosc_wierzcholkow))
print(parz(ilosc_wierzcholkow))
print(spojnosc(ilosc_wierzcholkow))


#CYKL HAMILTONA
V=[]
wynik=[]
def hamilton(wierzcholek):
    V.append(wierzcholek)
    if(len(V)==n):
        if(matrix[wierzcholek][V[0]]):
            wynik.append(V)
        else:
            V.remove(wierzcholek)
    for i in range(n):
        if i not in V and matrix[wierzcholek][i]:
            hamilton(i)

hamilton(0)
print (wynik)

#jeszcze trzeba nad tym popracowac
def make_connection(matrix, x, y):
    matrix[x][y] = 1
    matrix[y][x] = 1

def del_connection(matrix, x, y):
    matrix[x][y] = 0
    matrix[y][x] = 0

def Hamilton2(matrix, v, V, result, RESULT):
    V.append(v)
    # print('V',V)
    for w in range(len(matrix[v])):
        if matrix[v][w] == 1 and w not in V:
            del_connection(matrix, v, w)
            result = Hamilton2(matrix, w, V, result, RESULT)
            if result:
                RESULT.append(result)
                V.pop()
                if len(V) > 1:
                    last = V[-1]
                    make_connection(matrix, v, last)
    if len(V) == len(matrix) and matrix[v][0] == 1:
        # print('result:',V+[0])
        return V+[0]
    else:
        V.pop()
        # print(V)
        if len(V) > 1:
            last = V[-1]
            make_connection(matrix, v, last)

RESULT =[]
#Hamilton2(matrix[:],0,[],[], RESULT)
#print(RESULT)
