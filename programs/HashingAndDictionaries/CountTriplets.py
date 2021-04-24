# Hackerrank question link: https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps
from collections import Counter


def countTriplets(arr, r):
    rightMap = Counter(arr)
    leftMap = Counter()
    res = 0
    for i in arr:
        j = i // r
        k = i * r
        rightMap[i] -= 1
        if j in leftMap and k in rightMap and i % r == 0:
            res += leftMap[j] * rightMap[k]
        leftMap[i] += 1
    return res


if __name__ == '__main__':
    n, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(countTriplets(arr, r))
