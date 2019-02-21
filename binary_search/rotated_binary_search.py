def search_rotated_array(arr, search):
    
    pivot = arr[0]
    if search == pivot:
        return True
    
    start = 1
    end   = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        middle = arr[mid]

        #Match case
        if search == middle:
            return mid

        if search < middle and middle < pivot or \
            middle < pivot and pivot < search or \
            pivot < search and search < middle:
        
            #search left half    
            end = mid -1
        else:
            
            #search right half
            start = mid + 1

    return -1

print(search_rotated_array([4,5,6,7,0,1,2], 5))