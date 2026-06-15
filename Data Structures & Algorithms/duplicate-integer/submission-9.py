class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for each_num in nums:
            if (each_num in nums_dict):
                return True
            else:
                nums_dict[each_num] = True
        return False
