class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_index = 0
        end_index = 1
        while start_index < len(numbers)-1:
            # print ('start_index', start_index)
            end_index = start_index + 1
            while end_index < len(numbers):
                # print('end_index',end_index)
                if numbers[start_index] + numbers[end_index] == target:
                    return [start_index+1, end_index+1]
                end_index = end_index+1
            start_index=start_index+1

        return []