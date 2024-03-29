def insertionSort(lst):
    n = len(lst)
    for i in range(1,n):
        temp = lst[i]
        j = i-1

        while j>=0 and temp<lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1]=temp

arr = [64, 34, 89, 12, 22, 11, 9]
insertionSort(arr)
print(arr)
