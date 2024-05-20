"""
Problem statement:
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].
Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

E.g.,
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
"""
from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        # key is x , values are y coords in sorted order
        lines_parallel_to_y_axis = defaultdict(list)      
        # key is y , values are x cords in sorted order
        lines_parallel_to_x_axis = defaultdict(list)      

        for x,y in points:
            lines_parallel_to_y_axis[x].append(y)
            lines_parallel_to_x_axis[y].append(x)
    
        for line in lines_parallel_to_y_axis.values():
            line.sort()

        for line in lines_parallel_to_x_axis.values():
            line.sort()

    
        for x,y in points:
            # Find adjacent corner of rectangle with same x and finding y coord
            for prev_y in lines_parallel_to_y_axis[x]:
                if prev_y >= y:
                    continue

                # Find the other adjacent corner of rectangle 
                # with same y given points in and finding its x coord
                for prev_x in lines_parallel_to_x_axis[y]:
                    if prev_x >= x:
                        continue

                    # validate the coords of newly identified corners intersect
                    if prev_x in lines_parallel_to_x_axis[prev_y]:
                        min_rect_area = abs((x - prev_x) * (y - prev_y))
                        if min_rect_area < min_area:
                            min_area = min_rect_area
        if min_area == float('inf'):
            return 0
        else:
            return min_area   
