class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int high=0, low=0, res=INT_MAX, sum=0, n=nums.size(), len=0;
        while(high<n){
            sum+= nums[high];

            while(sum>=target){
                len = (high-low)+1;
                res = min(len, res);
                sum -= nums[low];
                low++;
            }
            high++;
        }
        return min(len,res);
    }
};