class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indx, each_num in enumerate(nums):
            temp = target - each_num
            try:
                return [indx, nums[indx+1:].index(temp)+len(nums[:indx+1])]
            except Exception as e:
                pass