def SelectionSort(arr):

    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j] :
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


temp = [6,7,9,1,2,4,3]

print(SelectionSort(temp))
