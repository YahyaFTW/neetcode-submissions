class Solution {
public:
    int pivotIndex(vector<int>& a) {
        int totalSum= 0;
        int leftSum = 0;
        int n = a.size();
        for(int i =0;i<n;i++){
             totalSum=totalSum+a[i];
        }
        for(int i=0;i<n;i++){
            int rightSum = totalSum - leftSum - a[i];
            if (rightSum == leftSum){
                return i;
            }
            leftSum=leftSum+a[i];
        }
        
        return -1;
    }
};