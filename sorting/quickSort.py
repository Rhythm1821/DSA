def quickSort(lst):
    n = len(lst)
    if n<=1:
        return lst
    else:
        pivot = lst[0]
        lesser = [x for x in lst[1:] if x<=pivot]
        greater = [x for x in lst[1:] if x>pivot]
        return quickSort(lesser) + [pivot] + quickSort(greater)
    
arr = [64, 34, 25, 12, 22, 11, 90]
arr = quickSort(arr)
print(arr)         