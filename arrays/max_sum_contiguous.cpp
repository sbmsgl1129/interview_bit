//https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

int Solution::maxSubArray(const vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int size = A.size();
    vector<int> sum_arr(size);
    vector<int>::iterator result;
    for(int i = 0; i< size ;i ++){
        if (i == 0){
            sum_arr[0] = A[0]; 
        }else {
            sum_arr[i] = max(A[i], sum_arr[i-1]+A[i]);
        }
    }
    result = max_element(sum_arr.begin(),sum_arr.end());
    return (*result);
}
