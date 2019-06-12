class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        
        n_map = {'0':0, '1':1, '2':2, '3':3, '4':4,
               '5':5, '6':6, '7':7, '8':8, '9':9 }
        
        carry = 0
        shift = 0
        l = []
        temp = []
        for digit_b in reversed(B):
            temp.extend([0]*shift) #zero padding at the start
            for digit_a in reversed(A):
                num   = n_map[digit_b]*n_map[digit_a]
                final_num = num + carry
                temp.append(final_num % 10)
                carry = final_num // 10
            
            #adding the final carry in the end and
            #extending the zeros depending on the base in which multiplication happened
            if carry != 0:
                temp.append(carry)
            
            temp.extend([0]*(len(A) + len(B) - len(temp)))
            
            #individual rows being added
            l.append(temp)
            
            #resetting/updating vars for next iteration
            shift += 1
            temp  = []
            carry = 0
         
        
        # finalling adding the cols to get the final result
        ans = []
        carry = 0
        
        rows = len(l)
        cols = len(l[0])
        
        for i in range(cols):
            s = carry
            for j in range(rows):
                    s += l[j][i]
                    
            ans.append(str(s%10))
            carry = s // 10
            
        
        if carry != 0:
            ans.append(str(carry)) 
            
        ans_s = ''.join(reversed(ans)).lstrip()
        return ans_s if ans_s else '0'
