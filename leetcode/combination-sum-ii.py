class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # this will hold all unique combinations that sum to target
        candidates.sort()  # sort first to make it easier to skip duplicates

        def dfs(i, cur, total):
            # If current combination sums to target, save a copy and return
            if total == target:
                res.append(cur[:])  # append a *copy* of cur
                return 
            
            # If total exceeds target OR we've run out of candidates, stop exploring
            if total > target or i >= len(candidates):
                return 
            
            # 1. Include candidates[i] in the combination
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()  # backtrack (remove last added element)

            # 2. Skip candidates[i]
            # Move i forward to skip duplicates of the same value
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # Explore further without including candidates[i]
            dfs(i + 1, cur, total)
        
        # Start DFS with index 0, empty combination, and total sum 0
        dfs(0, [], 0)
        return res