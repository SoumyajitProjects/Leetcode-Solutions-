class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res will hold all subsets
        res = []
        # subset is a temporary list to build the current subset
        subset = []

        def dfs(i):
            # Base case: if we've considered all elements
            if i >= len(nums):
                # append a *copy* of the current subset
                res.append(subset[:])
                return 

            # Decision 1: include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack: remove nums[i] from the subset
            subset.pop()

            # Decision 2: do NOT include nums[i] in the subset
            dfs(i + 1)
        
        # Start DFS from index 0
        dfs(0)
        return res