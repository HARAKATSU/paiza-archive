import math
cont = True
N = int(input())

while cont:
    s = list(str(N))
    s.reverse()
    s = int(''.join(s))
    newN = N + s

    r = int(math.floor(len(str(newN)) / 2))
    
    # 先頭からi文字目と末尾からi文字目が等しい回数
    cnt = 0
    
    for i in range(r):
        if str(newN)[i] == str(newN)[-i -1]:
            cnt += 1
        if cnt == r:
            print(newN)
            cont = False
    N = newN
