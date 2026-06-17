class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        res=[]

        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict[num]+1
            else:
                count_dict[num] = 1
        
        nums_count = [[val,key] for key, val in count_dict.items()]
        nums_count.sort()

        for i in range (len(nums_count)-k, len(nums_count)):
            res.append(nums_count[i][1])
        return (res)