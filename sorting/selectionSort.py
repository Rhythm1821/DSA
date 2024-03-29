def selectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if lst[j] < lst[minIndex]:
                minIndex = j
        lst[i],lst[minIndex] = lst[minIndex],lst[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print(arr)        