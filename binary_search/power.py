import functools

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        ##using the teachnique described here: https://bit.ly/2GqlenF 
        
        n_bin_str = "{0:b}".format(n)
        two_power_list = [2**idx for idx, ch in enumerate(reversed(n_bin_str)) if ch == '1']

        ##Power 0 case:
        if not two_power_list:
            return 1 % d

        x_mod_two_powers = { }
        prev_mod_two_power = 1
        for two_power in [2**i for i in range(len(n_bin_str))]:
            if two_power == 1:
                x_mod_two_powers[two_power] = x % d
            else:
                x_mod_two_powers[two_power] = (prev_mod_two_power * prev_mod_two_power) % d

            prev_mod_two_power = x_mod_two_powers[two_power]

        ##Power of python and FP
        return functools.reduce(lambda a,b: (a*b) % d, map(lambda two_power: x_mod_two_powers[two_power], two_power_list))           
