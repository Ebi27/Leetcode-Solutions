class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums[:] * 2 # Create a copy of nums and replicate it twice using the * operator. The time complexity is O(2n)
        return ans

        """
        If we want to save on space, we can just return the operation directly (return nums * 2 )
        """