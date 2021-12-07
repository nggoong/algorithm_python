heights = [int(input()) for i in range(9)]
heightsSum = sum(heights)


for i in range(9):
    copyArr = sorted(heights)
    for j in range(i + 1, 9):
        if heightsSum - (heights[i] + heights[j]) == 100:
            copyArr.remove(heights[i])
            copyArr.remove(heights[j])

            for k in copyArr:
                print(k)

            if len(copyArr) < 9:
                break


    
