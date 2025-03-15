memo = {}
def min_breaks(n, m):
    if (n, m) in memo:
        return memo[(n, m)]
    if n == 1 and m == 1:
        return 0
    if n == 1 or m == 1:
        return max(n, m) - 1
    result = min(min_breaks(n - 1, m) + m, min_breaks(n, m - 1) + n)
    memo[(n, m)] = result
    return result
print(min_breaks(2, 3))
print(min_breaks(3, 3))
print(min_breaks(1, 1))
