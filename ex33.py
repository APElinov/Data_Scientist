def power(n, m):
    if m == 0:
        return 1
    return 1 / n * power(n, abs(m) - 1)


print(power(-3, -3))
