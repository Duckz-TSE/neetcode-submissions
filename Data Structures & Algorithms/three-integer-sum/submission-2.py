class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        first = 0

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            second = i + 1
            third = len(nums) - 1
            while second < third:
                sum = nums[second] + nums[third]
                if (sum + num) == 0:
                    res.append([nums[i], nums[second], nums[third]])
                    second += 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                elif (sum + num) < 0:
                    second += 1
                else:
                    third -= 1
           

        return res