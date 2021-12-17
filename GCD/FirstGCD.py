def GCD(a, b):
    result = []
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            result.append(i)
    return max(result)


print(GCD(12, 48))