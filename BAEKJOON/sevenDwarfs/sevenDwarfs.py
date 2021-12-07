heights = [int(input()) for i in range(9)]
heightsSum = sum(heights)

copyArr = sorted(heights)

for i in range(9):
    for j in range(i + 1, 9):
        if heightsSum - (heights[i] + heights[j]) == 100:

            for k in range(9):
                if copyArr[k] == heights[i] or copyArr[k] == heights[j]:
                    continue
                else:
                    print(copyArr[k])


    
