class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * len(nums) * 2

        for i, num in enumerate(nums):
            ans[i + length] = num
            ans[i] = num
        return ans