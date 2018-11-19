// Input : X and Y co-ordinates of the points in order. 
// Each point is represented by (X[i], Y[i])

//https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

int cal_weight(vector<int> &X, vector<int> &Y, int i, int j){
    int weight;
    int d1, d2, d3;
    if(X[i] == X[j] )
        weight = abs(Y[i] - Y[j]);
    else if(Y[i] == Y[j]){
        weight = abs(X[i] - X[j]);
    }
    else{
        d1 = abs(X[i] - X[j]);
        d2 = abs(Y[i] - Y[j]);
        if(d1 < d2){
            d3 = min(abs(Y[j] - Y[i] + d1), abs(Y[j] - Y[i] - d1));
            weight  = d1+d3;
        }
        else {
            d3 = min(abs(X[j] - X[i] + d2), abs(X[j] - X[i] - d2));
            weight = d2+d3;
        }
    }
    return weight;
}

int Solution::coverPoints(vector<int> &X, vector<int> &Y) {
    int v = X.size();
    int i = 0, weight = 0;
    for(i =1 ; i< v; i++){
        weight += cal_weight(X,Y,i-1,i);  
    }
    return weight;
}
