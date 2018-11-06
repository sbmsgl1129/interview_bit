/* Link: https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/ */

int count_permutations(int num_digits_first_place, int total_digits, int integer_len){
    
    if(num_digits_first_place == 0){
        return 0;
    }
    
    return (num_digits_first_place)*pow(total_digits, integer_len - 1);
}

int num_ints_lesser_than_C_digit(vector<int> &digit_array, int C_digit, bool &is_C_digit_present){
    int count = 0;
    is_C_digit_present = false;
    
    for(int i : digit_array){
        if(i < C_digit){
            count++;
        }
        if(i == C_digit){
            is_C_digit_present = true;
            break;
        }
    }
    return count;
}

int Solution::solve(vector<int> &A, int B, int C) {
    
    //Some data that wouls be useful
    auto size = A.size();
    if(size == 0) return 0;
    
     //Will be used for calculating count
    int lowest_digit  = A[0];
    bool is_lowest_digit_zero = false;
    if(lowest_digit == 0){
       is_lowest_digit_zero = true; 
    }
    
    //Optimisation before we proceed
    
    //If the given C length is less than length of number required
    string C_str  = to_string(C);
    int C_str_len = C_str.length();
    if(C_str_len < B){
        return 0;
    }
    
    //If the given C length is greater than length of number required
    if(C_str_len > B){
        int num_first_digits;
        
        //First digit can't be 0 unless it is a single digit number
        if(B == 1){
            num_first_digits = size;
        }else{
            num_first_digits  = is_lowest_digit_zero ? (size-1) : size;
        }
       
        return count_permutations(num_first_digits, size, B);
    }
    
    int count = 0;
    int i = 0;
    bool is_C_digit_present = true; //if not we need not proceed, useful for next iteration
    while(B > 0 && is_C_digit_present){
        
        int num_digits_first+place = num_ints_lesser_than_C_digit(A, C_str[i] - '0', is_C_digit_present);
        
        //removing '0' as it can't be first digit
        if(i == 0 && B > 1 && is_lowest_digit_zero){
            num_digits_first_place -= 1;   
        }
        
        count += count_permutations(num_digits_first_place, size, B);
        
        i++;
        B--;
    }
    
    return count; 
}
