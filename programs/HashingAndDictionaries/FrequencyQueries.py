# Hackerrank question link: https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

from collections import Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    counter = Counter()
    freqCounter = Counter()
    for x, y in queries:
        val = counter[y]
        if x == 1:
            freqCounter[val] = max(freqCounter[val] - 1, 0)
            freqCounter[val + 1] += 1
            counter[y] = val + 1
        elif x == 3:
            yield 1 if freqCounter[y] > 0 else 0
        elif val:
            freqCounter[val] = max(freqCounter[val] - 1, 0)
            freqCounter[val - 1] += 1
            counter[y] = val - 1


if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
    print('\n')