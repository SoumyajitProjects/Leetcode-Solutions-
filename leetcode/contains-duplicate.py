class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Optimal Solution Using a Hashset:
        # Create a set which keeps track of the elements
        seen = set()

        # Iterate through the list:
        for n in nums:
            # If the element is already in the set it is a duplicate so we return True
            if n in seen:
                return True 
            # Else it is not in the list set and we add it 
            seen.add(n)
        return False
        
    #Brute Force Solution:
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False
        """