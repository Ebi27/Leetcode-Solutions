    
"""
    sol 1 
    - sort the numbers in ascending order
    - Use two pointers. one at the begining and one next to it.
    - Compare the first pointer to the second, if same, return true 
    - if not, move pointers forward and repeat 
pro = we get to work with sorted array adj of each other 
con = we trade off on runtime. Sorting time makes this a bad idea O(n log n)

    sol 2 
    - use dict 
    - when we encounter a number, we put it in the dict and initialize a count as the key
    - When we move on to the next number, we check if it is already present in our dict 
    - if it is, we have a duplicate, we return true 
pro = adding, accessing items in O(1) time 
con = having to create key and values for each item inserted. We trade off on space to store our dict 

    sol 3 
    - use a set 
    - this works because a set cannot contain a duplicate   
    - check if the ele is present, if it is , then it's a duplicate 
    - else, add it 
    - if after the entire loop, no duplicate, then return false 
pro = similar to sol 2 plus only adding items, no need for creating pairs 
con = just the space tradeoff 

Verdict; Optimized solution depends on if we want to tradeoff time or space, 
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = set()

        for num in nums:
            if num in hashmap:
                return True 
            else: 
                hashmap.add(num)
        return False
