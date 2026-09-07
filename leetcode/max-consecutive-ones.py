class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0 
        for n in nums:
            if n == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        return max(res, count)