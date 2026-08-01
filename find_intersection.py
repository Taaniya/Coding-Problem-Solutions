"""
Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
"""

import ast
from typing import List, Union

def FindIntersection(strArr: List[str]) -> Union[str, bool]:
    arr_1, arr_2 = [x.strip() for x in strArr[0].split(",")], [x.strip() for x in strArr[1].split(",")]
    common_num = set(arr_1).intersection(arr_2)

    if len(common_num):
        common_num_arr = list(common_num)
        common_num_arr.sort(key=lambda x: ast.literal_eval(x))
        return ",".join(common_num_arr)
    else:
        return False


if __name__ == "__main__":
    print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))         # 1,4,13
    print(FindIntersection(["1, 5, 6, 7, 10, 11, 12", "5, 6, 8, 11, 17"])) # 5,6,11
    print(FindIntersection(["2, 3, 4", "3"]))                              # 3
    print(FindIntersection(["1, 2, 4, 5, 6, 9", "2, 3, 4, 8, 10"]))        # 2,4
