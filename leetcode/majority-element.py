class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution using Hash-Map 
        # Initialize a Hashmap to keep count of value to the number of occurances of that value (val -> count)
        count = {}

        # Loop through the array and build out the freq. map storing all values and their occurances
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Now loop through the freq. map and check if any of the values has a count greater than n/2
        for n in count:
            if count[n] > len(nums) // 2:
                return n
        
        """
        TC -> O(N), the loop to count freq's: O(N), the loop to find majority element in hashmap: O(N), worst Case
        SC -> O(N), the dictionary stores up to n keys in the worst case (all elements unqiue)
        """