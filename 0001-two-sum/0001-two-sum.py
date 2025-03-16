class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for i, num in enumerate(nums):
            remainder = target - num 
            if remainder in hashmap: 
                return hashmap[remainder], i 
            else: 
                hashmap[num] = i 

        return []
        