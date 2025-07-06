class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with 1s
        res = [1] * len(nums)

        # Step 1: Calculate prefix products
        # This loop sets res[i] to the product of all elements to the left of i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix           # res[i] holds product of all elements to the left
            prefix *= nums[i]        # update prefix to include nums[i] for the next index

        # Step 2: Calculate postfix products and multiply with existing values in res
        # This loop goes from right to left
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix        # multiply res[i] by product of all elements to the right
            postfix *= nums[i]       # update postfix to include nums[i] for the next left index

        return res