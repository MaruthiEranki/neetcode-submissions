class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        temp_seq = 1
        seq = 1
        if len(nums) == 0:
            return 0
        for index in range(0, len(nums)-1):
            if nums[index+1] - nums[index] == 1:
                temp_seq = temp_seq+1
            else:
                if temp_seq > seq:
                    seq = temp_seq
                temp_seq = 1
                
        seq = temp_seq if temp_seq>seq else seq 
        return seq
        