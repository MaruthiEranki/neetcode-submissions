class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start_index = 0
        end_index = start_index + 1
        max_water_container = 0
        area = 0
        while start_index < len(heights)-1:
            end_index = start_index + 1
            while end_index < len(heights):
                distance = end_index - start_index
                least_bar = heights[start_index] if heights[start_index] < heights[end_index] else heights[end_index]
                area = distance * least_bar
                max_water_container = area if area > max_water_container else max_water_container
                end_index = end_index + 1
            start_index = start_index + 1
        return max_water_container