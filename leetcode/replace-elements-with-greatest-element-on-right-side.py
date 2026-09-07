class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Base Case: last element is -1
        rightMax = -1

        # Iterate through array in reverse order
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr