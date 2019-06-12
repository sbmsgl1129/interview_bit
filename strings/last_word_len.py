class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        
        last_word_len = 0
        current_word_len = 0
        
        for char in A:
            if char == ' ':
                if current_word_len != 0:
                    last_word_len = current_word_len
                    current_word_len = 0
            else:
                current_word_len += 1
        
        #As last word wont have any space at the end
        if current_word_len != 0:
            last_word_len  = current_word_len
        
        return last_word_len
