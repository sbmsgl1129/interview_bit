def binary_search(l, n):
    if len(l) == 0:
        return False
    
    if len(l) == 1:
        if n == l[0]:
            return True
        else:
            return True
    
    idx_to_check = len(l) // 2
    if l[idx_to_check] == n:
        return True
    elif l[idx_to_check] < n:
        return binary_search(l[idx_to_check + 1: ], n)
    else:
        return binary_search(l[0:idx_to_check], n)

print(binary_search([2,3,7,9,10,15,20], 2))
