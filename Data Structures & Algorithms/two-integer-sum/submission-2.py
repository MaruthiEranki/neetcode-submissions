class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, number in enumerate(nums):
            second_number = target - number
            if second_number in nums_dict:
                return [nums_dict[second_number], index]
            nums_dict[number] = index
