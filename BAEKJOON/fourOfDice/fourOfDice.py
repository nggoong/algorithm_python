answer = []

for i in range(int(input())):
    arr = list(map(int, (input().split())))
    arr.sort()
    if len(set(arr)) == 1:
        answer.append(50000 + (arr[0] * 5000))

    elif len(set(arr)) == 2:
        if arr[1] != arr[2]:
            answer.append(2000 + (arr[0] * 500) + (arr[2] * 500))

        elif arr[1] == arr[2]:
            answer.append(10000 + (arr[1] * 1000))

        
    elif len(set(arr)) == 3:
        if arr[0] == arr[1] or arr[2] == arr[0]:
            answer.append(1000 + (arr[0] * 100))

        elif arr[1] == arr[2]:
            answer.append(1000 + (arr[1] * 100))
    elif len(set(arr)) == 4:
        answer.append(arr[3] * 500)


print(max(answer))


