class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        Optimized Solution: Using Hashmap 
        TC -> O(N), each element is visted once
        SC -> O(N), storing up to N elements in the hash map 
        """ 
        # Initialize a dictionary to store prev seen numbers and their indices (val -> index)
        prevSeen = {}

        # Loop through each number in the array along with its index
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target 
            diff = target - n 
            if diff in prevSeen:
                # If the required number to reach the target has already been seen, return the indices of that number and
                # the current number
                return [prevSeen[diff], i]
            # Else store the current number and its index in the dictionary 
            prevSeen[n] = i
            

        """
        Brute Force Solution 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        TC -> O(N^2)
        SC -> O(1)
        """