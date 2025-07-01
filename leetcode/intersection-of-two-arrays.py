class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a set to store elements in both arrays 
        res = []

        # Loop through the first array 
        for i in nums1:
            # Check to see if the element is in the second array and not in the final set 
            if i in nums2 and i not in res:
                # if so we append the element to the set 
                res.append(i)
        # Loop exists and we return the resulting set 
        return res

        """ 
        TC:
        Outer loop runs for each element in nums1: → O(n)
        i in nums2 takes O(m) in worst case (linear search)
        i not in res also takes O(r), where r is size of res (at most min(n, m))
        TC = O(n * (m + r)) ≈ O(n * m)

        SC: 
        res: stores unique intersection elements → max O(min(n, m))
        SC = O(r) ≈ O(min(n, m))
        """