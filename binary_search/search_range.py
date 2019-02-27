def find_occurence(list, search, occurence_type):
    
    start = 0
    end   = len(list) - 1

    idx = -1
    while start <= end:
        mid = (start + end) // 2
        mid_val = list[mid]

        if mid_val == search:
            idx = mid
            
            ##if left, then search more left, if right, then search more right
            if occurence_type == 1:
                end = mid - 1
            else:
                start = mid + 1
        
        if mid_val > search:
            end = mid -1
        
        if mid_val < search:
            start = mid + 1

    return idx

class Solution:
    
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        LEFT = 1
        RIGHT = 2

        low  = find_occurence(A, B, LEFT)
        high = find_occurence(A, B, RIGHT)

        return [low, high]

