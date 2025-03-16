class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        arr=set()
        for i in range(0,len(nums)):
            arr.add(nums[i]) # add() is used for set and append() for list

        arr=sorted(arr)
        del nums[:]   # we'll get nums as a reference i.e. empty list

        nums.extend(arr)
        '''

        x = 1
        for i in range(len(nums)-1):
	        if(nums[i]!=nums[i+1]):
		        nums[x] = nums[i+1]
		        x+=1
        return(x)
