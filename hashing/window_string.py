from collections import defaultdict
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        
        B_dict = defaultdict(int)
        for char in B:
            B_dict[char] += 1
        B_unique_chars = len(B_dict)
        
        ans_range = (0,0)
        min_window_len = float('inf')
        num_chars_covered = 0
        
        right_move = 1
        
        i = 0
        j = 0
        while j < len(A):
            if right_move == 1:
                if A[j] in B_dict:
                    B_dict[A[j]] -= 1
                    if B_dict[A[j]] == 0:
                        num_chars_covered += 1
                
                        if num_chars_covered == B_unique_chars:
                            if (j - i + 1) < min_window_len:
                                min_window_len = j - i + 1
                                ans_range = i, j + 1
                            
                            right_move = 0
                            continue
                    
                j += 1
            else:
                if A[i] in B_dict:
                    B_dict[A[i]] += 1
                    if B_dict[A[i]] > 0:
                        
                        num_chars_covered -= 1
                        right_move = 1
                        
                        if (j - i + 1) < min_window_len:
                            min_window_len = j - i + 1
                            ans_range = i, j + 1
                        
                        i += 1
                        j += 1
                        continue
                    
                i += 1
        
        return A[ans_range[0]:ans_range[1]]

