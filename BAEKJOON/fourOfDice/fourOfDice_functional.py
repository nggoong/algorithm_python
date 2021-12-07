def func(arr):
    result = 0
    if len(set(arr)) == 1:
        result = 50000 + (arr[0] * 5000)

    elif len(set(arr)) == 2:
        if arr[1] == arr[2]:
            result = 10000 + (arr[1] * 1000)

        elif arr[1] != arr[2]:
            result = 2000 + (arr[0] * 500) + (arr[2] * 500)
        
    elif len(set(arr)) == 3:
        if arr[0] == arr[1]:
            result = 1000 + (arr[0] * 100)

        elif arr[1] == arr[2]:
            result = 1000 + (arr[1] * 100)
        else:
            result = 1000 + (arr[2] * 100)

    elif len(set(arr)) == 4:
        result = arr[3] * 100

    return result

N = int(input())
answer = []
for i in range(N):
    arr = sorted(list(map(int, (input().split()))))
    answer.append(func(arr))
    
print(max(answer))




