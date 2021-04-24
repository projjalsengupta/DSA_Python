# Hackerrank question link: https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming


def maxSubsetSum(arr):
    dp = [0] * (len(arr) + 1)
    for index in range(1, len(arr) + 1):
        prevIndex = index - 2
        if prevIndex >= 0:
            dp[index] = max(dp[index - 1], dp[prevIndex] + arr[index - 1], dp[prevIndex], arr[index - 1], 0)
        else:
            dp[index] = max(dp[index - 1], arr[index - 1], 0)
    return dp[len(arr)]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(str(res) + '\n')