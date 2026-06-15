class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        prefix = 1
        postfix = 1

        for index, each_num in enumerate(nums):
            result[index] = prefix
            prefix = prefix*each_num

        for index in range(len(nums)-1, -1, -1):
            result[index] = result[index]*postfix
            postfix = postfix*nums[index]

        return result
