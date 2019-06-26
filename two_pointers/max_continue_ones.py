class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
	    
	            
        start, end = 0,0
        max_len = 0
        
        i = 0
        j = 0
	       
	    # Handling normal cases    
	    temp = B
	    while j < len(A):
	        if A[j] == 0:
	            if temp == 0:
	                if (j - i) > max_len:
                       # Checking if this run has greater than max till now,
                       # if so replace it with current max
                        max_len = j - i
                        start,end = i,j
                    
                    if B == 0:
                        while j < len(A) and A[j] == 0:
                            j += 1
                        i = j
                    else:
                        if A[i] == 0:
                            temp = 1
                    
                        i += 1

                elif temp != 0:
                    temp -= 1
                    j += 1

	        elif A[j] == 1:
	            j += 1
	       
	       
	    # for the last run
	    if (j - i) > max_len:
	        max_len = j - i
	        start,end = i,j
	   
	    return list(range(start,end))
