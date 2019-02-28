
class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        
        lcp = []
        s = A[0] # take a string from list

        #Iterate over all the chars of the string and check if they are matching with other chars.
        #when it doesn't we will break
        for idx, ch in enumerate(s):
            
            if not all([True if idx < len(string) and string[idx] == ch else False for string in A[1:]]):
                break
                
            lcp.append(ch)
                       
        return ''.join(lcp)