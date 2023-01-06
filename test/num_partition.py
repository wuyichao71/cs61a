def num_partition(n, k):
    if n < 0:
        return 0
    elif k == 1:
        return 1
    else:
        return num_partition(n - k, k) + num_partition(n, k - 1)

print(num_partition(12, 3))
