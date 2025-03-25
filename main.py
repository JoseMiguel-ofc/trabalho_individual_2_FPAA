def maxmin_select(arr, left, right):
    if left == right: 
        return arr[left], arr[left]
    
    if right - left == 1:  
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    return min(min1, min2), max(max1, max2)

arr = [3, 1, 9, 7, 5, 11, 2, 8]
min_val, max_val = maxmin_select(arr, 0, len(arr) - 1)
print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
