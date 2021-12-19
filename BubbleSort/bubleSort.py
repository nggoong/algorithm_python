def BubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

temparr = [6,7,9,1,2,4,3,5,8]
print(BubbleSort(temparr))
