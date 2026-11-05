class Solution {
public:
    int subarraySum(vector<int>& a, int k) {
        unordered_map<int,int> sumMap;
        // vector<int> pre(a.size(),0);
        int count=0,psum=0;
        sumMap[0]=1;

        for(int i=0;i<a.size();i++){
            psum+=a[i];
            int diff = psum-k;
            if(sumMap.contains(diff)){
                count+=sumMap[diff];
            }
            sumMap[psum]++;
        }
        return count;
    }
};