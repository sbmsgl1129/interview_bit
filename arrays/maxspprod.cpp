//https://www.interviewbit.com/problems/maxspprod/

int Solution::maxSpecialProduct(vector<int> &A) {
    int size = A.size();
    
    vector<int> lsv(size,0);
    stack<pair<int,int>> prev_largest;
    for(int i = 0; i < size; i++){
        
        while(!prev_largest.empty()){
            if(prev_largest.top().first > A[i]){
                lsv[i] = prev_largest.top().second;
                prev_largest.push(make_pair(A[i],i));
                break;
            }else{
                prev_largest.pop();
            }    
        }
        if(prev_largest.empty()){
           prev_largest.push(make_pair(A[i],i));
           lsv[i] = 0;    
        }
    }
    
    vector<int> rsv(size,0);
    stack<pair<int,int>> next_largest;
    for(int i = size - 1; i >= 0; i--){
        
        while(!next_largest.empty()){
            if(next_largest.top().first > A[i]){
                rsv[i] = next_largest.top().second;
                next_largest.push(make_pair(A[i],i));
                break;
            }else{
                next_largest.pop();
            }    
        }
        if(next_largest.empty()){
           next_largest.push(make_pair(A[i],i));
           rsv[i] = 0;    
        }
    }
    
    long long max_s_prod = 0;
    for(int i = 0; i < size; i++){
        long long s_product = lsv[i] * rsv[i];
        if(s_product > max_s_prod){
            max_s_prod = s_product;
        }
    }
    
    
    return (max_s_prod % 1000000007);
}

