class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # this will store all the permutations

        # Base case: if there's only one number, return it as the only permutation
        if len(nums) == 1:
            return [nums[:]]  # make a copy of nums and return inside a list

        # Loop through all positions in nums
        for i in range(len(nums)):
            # Remove the first element and save it as n
            n = nums.pop(0)

            # Recursively get all permutations of the remaining numbers
            perms = self.permute(nums)

            # For each smaller permutation, add the removed number back at the end
            for perm in perms:
                perm.append(n)

            # Add all those updated permutations into the result
            res.extend(perms)

            # Put the removed number back into nums so the next loop iteration works
            nums.append(n)

        # After looping through all numbers, return the full list of permutations
        return res