class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for k in range(len(nums)):
            if k>0 and nums[k] == nums[k-1]:
                continue
            # [-4, -1, -1, 0, 1, 2]
            i, j = k+1, len(nums)-1
            sum = -nums[k]
            while j>i:
                if nums[i]+nums[j]>sum:
                    j-=1

                elif nums[i]+nums[j]<sum:
                    i+=1
                
                else:
                    l.append([nums[i], nums[j],nums[k]])
                    i+=1
                    j-=1

                    while i < j and nums[i]==nums[i-1]:
                        i+=1
                    while i < j and nums[j]==nums[j+1]:
                        j-=1
            
        return l;
