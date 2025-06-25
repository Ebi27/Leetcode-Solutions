class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #ans = nums * 2 
        return nums * 2 

        """
        we can simply just return nums * 2 without creating the ans variable. Shocker. The memory is better than using the nums[:] which creates a shallow copy of the original list and assigns it to ans before repeating it again. 
        """