class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        
        low, high = -1, -1
        max_seq_len = high - low
        
        sum_arr = []
        prev_sum = 0
        for num in A:
            sum_arr.append(prev_sum + num)
            prev_sum = prev_sum + num
        
        #print(sum_arr)
        
        dic = {}
        dic[0] = -1 #important edge case
        for idx,num in enumerate(sum_arr):
            if num in dic:
                seq_len = idx - dic[num]
                if seq_len > max_seq_len:
                    max_seq_len = seq_len
                    low = dic[num] + 1
                    high = idx
            else:
                dic[num] = idx
        
        return A[low:high+1]
