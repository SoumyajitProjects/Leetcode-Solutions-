class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count the frequency of each element
        count = {}

        # Create a list of empty lists to act as frequency "buckets"
        # Index i of freq will store elements that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in nums
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Place each number into the correct frequency bucket
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []  # This will hold the top K frequent elements

        # Iterate from highest possible frequency to lowest (reverse)
        for i in range(len(freq) - 1, 0, -1):
            # For every number with current frequency i
            for num in freq[i]:
                res.append(num)  # Add it to result list
                if len(res) == k:  # Once we have k elements, return
                    return res