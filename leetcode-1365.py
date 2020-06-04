class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result =[]
        new_nums = sorted(nums)
        for i in nums:
                result.append(new_nums.index(i))
        return result        
            
