class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        indices = []
        for each_num in nums_set:
            indices.append([index for index, value in enumerate(nums) if value == each_num])

        indices.sort(key=len)
        
        indices = indices[-k:]
        print(indices)
        for indx, each_indx in enumerate(indices):
            indices[indx] = nums[indices[indx][0]]
        print(indices)
        return indices