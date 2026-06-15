class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_index = 0
        end_index = len(numbers)-1

        while start_index < end_index:
            sum_val = numbers[start_index] + numbers[end_index]
            if sum_val == target:
                return [start_index+1, end_index+1]
            if sum_val>target:
                end_index = end_index - 1
            else:
                start_index = start_index + 1

        return []