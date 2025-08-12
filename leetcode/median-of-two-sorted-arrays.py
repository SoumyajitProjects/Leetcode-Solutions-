class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2  # number of elements on the left side of the combined partition

        # Ensure A is the shorter array so our binary search is on the smaller space
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1  # binary search over indices of A (partition i sits between i and i+1)
        while True:
            i = (l + r) // 2          # partition index in A (left part ends at i)
            j = half - i - 2          # derived partition index in B so that left parts total = half

            # Values just to the left/right of the partitions, with sentinels for out-of-bounds
            A_left  = A[i]     if i >= 0 else float("-inf")
            A_right = A[i + 1] if (i + 1) < len(A) else float("inf")
            B_left  = B[j]     if j >= 0 else float("-inf")
            B_right = B[j + 1] if (j + 1) < len(B) else float("inf")

            # Correct partition if every left value ≤ every right value
            if A_left <= B_right and B_left <= A_right:
                if total % 2:  # odd total → median is the next element on the right
                    return min(A_right, B_right)
                # even total → average of the max of lefts and min of rights
                return (max(A_left, B_left) + min(A_right, B_right)) / 2     

            # If A_left is too big, move partition i left
            elif A_left > B_right:
                r = i - 1
            # Otherwise move partition i right
            else:
                l = i + 1