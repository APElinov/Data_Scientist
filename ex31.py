def sum_of_seq(n, m):
    count: int = 0
    for i in range(0, n + 1, m):
        count += i
    count = n if count == 0 else count
    return count


print(sum_of_seq(5, 1))
print(sum_of_seq(5, 9))
print(sum_of_seq(8, 2))