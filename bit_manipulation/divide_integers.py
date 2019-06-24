class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        
        is_ans_negative = 0
        if (A < 0 and B > 0) or (A > 0 and B < 0):
            is_ans_negative = 1
            
        A = abs(A)
        B = abs(B)
     
        ans = 0
        while A > 0:
            temp = B
            i = 0
            while (temp << i) <= A:
                i += 1
            
            if i == 0:
                break
            
            ans |= (1 << (i-1))
            A   -= (B << (i-1))
            
        
        ans = -1*ans if is_ans_negative else ans
        
        if ans > (2**31 - 1):
            return 2**31 - 1
        if ans < -(2**31):
            return 2**31 - 1
            
        return ans

