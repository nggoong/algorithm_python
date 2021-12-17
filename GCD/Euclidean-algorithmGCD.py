def GCD(a, b):
    if a < b:
        if b % a == 0:
            return a
        else:
            GCD(a, b % a)

    elif a > b:
        if a % b == 0:
            return b

        else:
            GCD(b, a % b)


print(GCD(48, 12))