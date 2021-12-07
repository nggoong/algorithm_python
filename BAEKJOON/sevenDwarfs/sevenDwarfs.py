heights = [0] * 9
heightsSum = 0
for i in range(9):
    height = int(input())
    heights[i] = height
    heightsSum += height



for i in range(9):
    copyArr = []
    for j in range(i + 1, 9):
        if heightsSum - (heights[i] + heights[j]) == 100:
            copyArr = sorted(heights)
            copyArr.remove(heights[i])
            copyArr.remove(heights[j])
            
            for k in copyArr:
                print(k)


    
