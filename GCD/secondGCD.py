def GCD(a, b):
    result = 0
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            result = i
            break

    return result


print(GCD(12,48))
