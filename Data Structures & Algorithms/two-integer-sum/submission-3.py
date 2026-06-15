class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_ind = {}
        for i in range (0, len(nums)):
            if target - nums[i] in val_ind:
                return [val_ind[target-nums[i]], i]
            if nums[i] not in val_ind:
                val_ind[nums[i]] = i
