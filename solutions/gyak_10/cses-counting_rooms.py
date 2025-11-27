#gráfok, iterativ dfsel

n,m=map(int,input().split())
terulet=[input() for i in range(n)]

def keres(s,o,ellenorzo):
    stack=[(s,o)]
    while stack:
        s, o = stack.pop()
        lista = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i,j in lista:
            if o+j>m-1 or s+i>n-1 or o+j<0 or s+i<0:
                continue
            if terulet[s + i][o + j]== "." and not ellenorzo[s + i][o + j]:
                ellenorzo[s+i][o+j] = True
                stack.append((s+i,o+j))
def main():
    hanydb=0
    marellenorzott=[[False for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if terulet[i][j]== "." and not marellenorzott[i][j]:
                marellenorzott[i][j] = True
                keres(i,j,marellenorzott)
                hanydb+=1
    print(hanydb)

main()