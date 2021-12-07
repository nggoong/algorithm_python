N = int(input())

multi = -1
count = 0
answer = 0

if N < 10:
    answer = N

elif N >= 10:
    tempN = N
    while tempN >= 10:
        count += 1
        multi += 1
        answer += 9 * count * (10 ** multi)
        tempN = int(tempN / 10)
        

    count += 1
    multi += 1
    garbage = (N - (10 ** multi)) + 1
    answer += garbage * count
    
    print(answer)

    



