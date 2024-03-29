def bubbleSort(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                

def modifiedBubbleSort(lst:list):
    flag=False
    for i in range(1,len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag=True
        if not flag:
            break

arr = [64, 34, 25, 12, 22, 11, 90]

modifiedBubbleSort(arr)
print(arr)

