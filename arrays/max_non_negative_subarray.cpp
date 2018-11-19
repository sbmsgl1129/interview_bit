//https://www.interviewbit.com/problems/max-non-negative-subarray/

vector<int> Solution::maxset(vector<int> &A) {
   
   int length = A.size();
   
   pair<vector<int>, long long> solution = {vector<int>(),0};
   pair<vector<int>, long long> temp     = {vector<int>(),0};
   
   for(int i = 0; i < length; i++){
        if(A[i] < 0){
            if(temp.second > solution.second){
                solution = temp;    
            }else if(temp.second == solution.second){
                if(temp.first.size() > solution.first.size()){
                    solution = temp;
                }
            }
            
            temp.first.clear();
            temp.second = 0;
        
        }else{
            temp.first.push_back(A[i]);
            temp.second += A[i];
        }
   }
  
  //Final Check
  if(temp.second > solution.second){
        solution = temp;    
  }else if(temp.second == solution.second){
        
        if(temp.first.size() > solution.first.size()){
            solution = temp;
        }
  }

  return solution.first;
    
}

