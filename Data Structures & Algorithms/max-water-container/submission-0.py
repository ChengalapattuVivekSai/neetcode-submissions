class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left =0
        right =len(heights)-1

        max_area =0

        while  left < right:

            height_water = min(heights[left],heights[right])

            width = right - left

            total_area = height_water * width

            max_area = max(max_area,total_area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return max_area
        