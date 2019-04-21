#Uses python3

import sys

def lcs2(a, b):   
    dp_result = [[0 for j in range(b+1)] for i in range(a+1)]
    for x in range(1, a+1):
        for y in range(1, b+1):
            if a[x-1] == b[y-1] and b[y-1] == c[z-1]: 
                dp_result[x][y] = dp_result[x-1][y-1] + 1
            else:
                dp_result[x][y] = max(dp_result[x-1][y], dp_result[x][y-1], dp_result[x][y])

    return dp_result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
