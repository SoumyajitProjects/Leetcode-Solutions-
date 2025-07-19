class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # Stores all valid combinations that sum to target

        def dfs(i, cur, total):
            # Base case: if total equals target, we found a valid combination
            if total == target:
                res.append(cur.copy())  # Make a copy since cur is mutable
                return 
            
            # If we've gone past the array or total has exceeded the target, stop exploring
            if i >= len(nums) or total > target:
                return 
            
            # Include nums[i] in the current combination
            cur.append(nums[i])
            # Continue exploring with the same index `i` (can reuse same element)
            dfs(i, cur, total + nums[i])
            # Backtrack: remove the last added element and try the next index
            cur.pop()
            dfs(i + 1, cur, total)  # Exclude nums[i] and move to next index

        # Start DFS from index 0 with empty path and total 0
        dfs(0, [], 0)
        return res