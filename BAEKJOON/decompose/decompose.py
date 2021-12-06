num = int(input())
result = 0

for i in range(num - 54, num - 1):
    a = 0
    temp = i
    answer = i
    while temp >= 10:
        a = temp % 10
        temp = int(temp / 10)
        answer += a

    answer += temp

    if answer == num:
        result = i
        break
            

print(result)



                