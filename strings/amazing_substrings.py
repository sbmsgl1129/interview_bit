class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        vowel_positions = [idx if char in vowels for idx, char in enumerate(A)]

        str_len = len(A)
        num_amazing_substrings = 0
        for start_pos in vowel_positions:
            num_amazing_substrings += str_len - start_pos
            num_amazing_substrings %= 10003
        
        return num_amazing_substrings
