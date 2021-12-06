
def Fibo(n):
    if n == 1 or n == 2:
        return 1

    else:
        return Fibo(n-2) + Fibo(n-1)


print(Fibo(3))





def Fibo2(n):
    answer = [1, 1]
    result = 0
    if n == 1 or n == 2:
        return 1

    else:
        for i in range(3, n + 1):
            result = answer[0] + answer[1]
            # answer[0] = answer[1]
            # answer[1] = result
            answer[0], answer[1] = answer[1], result

    return result


print(Fibo2(4))




