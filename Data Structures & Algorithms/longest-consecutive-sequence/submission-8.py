class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        count = 0
        longest = 0
        
        for num in num_set:
            if num-1 not in num_set:
                count =1
                while num+count in num_set:
                    count= count+1
            longest=max(longest, count)
        return longest

