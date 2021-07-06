"""
*    author:  kattsun
*    created: 07-07-2021 07:04:45
"""
import math
def main():
    S = input().strip()
    num = '' # 数字の文字列
    rep = [1]
    atoz = dict(zip([chr(i) for i in range(97, 123)], [0] * 26))
    print(atoz)
    for c in S:
        # print(c)
        if c in '1234567890':
            num += c
        elif c == '(':
            rep.append(int(num))
            num = ''
        elif c == ')':
            del rep[-1]
        else:
            if num == '':
                atoz[c] += math.prod(rep)
            else:
                rep.append(int(num))
                atoz[c] += math.prod(rep)
                del rep[-1]
                num = ''
        # print(rep, num)
    # print(atoz)
    for k,v in atoz.items():
        print(k,v)

if __name__ == '__main__':
    main()