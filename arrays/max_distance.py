#https://www.interviewbit.com/problems/max-distance/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        size = len(A)
        val_index_arr = [(val, idx) for idx, val in enumerate(A)]
        val_index_arr.sort(key=lambda x: x[0])
        
        #print(val_index_arr)
        
        max_idx_right_arr = [0]*size
        for i in range(size-1, -1, -1):
            if i == size - 1:
                max_idx_right_arr[i] = val_index_arr[i][1]
            else:
                max_idx_right_arr[i] = val_index_arr[i][1] if val_index_arr[i][1] > max_idx_right_arr[i + 1] else max_idx_right_arr[i + 1]
        
        #print(max_idx_right_arr)
        return max([(j - i) for i, j in zip([idx for val, idx in val_index_arr], max_idx_right_arr)])
