def binarySearch(lst:list,n:int):
    l,r = 0,len(lst)-1 
    mid = len(lst) // 2
    while l<=r:
        if lst[mid]>n:
            r = mid - 1
        elif lst[mid]<n:
            l = mid + 1
        else:
            return mid

arr=[1,2,3,4,5]        
res = binarySearch(arr,3)
print(res)