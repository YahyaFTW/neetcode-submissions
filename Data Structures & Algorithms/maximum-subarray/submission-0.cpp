class Solution {
public:
    int maxSubArray(vector<int>& nums) {
		int best = -10001, ans =nums[0];

		for (int i =0;i<nums.size();i++){
			best=max(nums[i], nums[i]+best);
			ans=max(ans,best);
		}
		return ans;
    }
};
