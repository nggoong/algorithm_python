

for i in range(int(input(""))):
    global n, m
    global numberOfFriend
    count = 0
    answer = 0
    friendList = []
    tempn, tempm = input("").split()
    n = int(tempn)
    m = int(tempm)
    print(m)
    choicenumber = [0] * n

    numberOfFriend = input("")  # 친구 목록
    numberOfFriend = numberOfFriend.replace(" ", "")
    print(numberOfFriend, "입니다")
    for i in range(0, m - 2, 2):
        if(choicenumber[int(numberOfFriend[i])] != 1 or choicenumber[int(numberOfFriend[i])] != 1):
            choicenumber[int(numberOfFriend[i])] = 1
            choicenumber[int(numberOfFriend[i + 1])] = 1
            count += 2
            print('실험')
        elif (count == n):
            answer += 1
            print('실험 끝')
            print(answer)
            
            break
