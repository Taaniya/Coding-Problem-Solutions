"""
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true

Solution Approach -
* Checks only consecutive digit pairs in the string
* Counts question marks between each consecutive pair that sums to 10
* Returns False if any such pair doesn't have exactly 3 question marks
* Returns False if no pairs sum to 10
"""
import re

def QuestionsMarks(strParam: str) -> bool:
  # Find all digit positions and their values
  digits = []
  for i, char in enumerate(strParam):
    if char.isdigit():
      digits.append((i, int(char)))
  
  # Check consecutive digit pairs only
  has_pair_adding_to_10 = False
  for i in range(len(digits) - 1):
    pos1, val1 = digits[i]
    pos2, val2 = digits[i + 1]
    
    if val1 + val2 == 10:
      has_pair_adding_to_10 = True
      # Count question marks between the two digits
      substring = strParam[pos1 + 1:pos2]
      qmark_count = substring.count('?')
      
      # Must have exactly 3 question marks
      if qmark_count != 3:
        return False
  
  # Return false if no pairs add up to 10
  return has_pair_adding_to_10


if __name__ == "__main__":
    print(QuestionsMarks("aa6?9"))                          # False
    print(QuestionsMarks("arrb6???4xxbl5???eee5"))          # True
    print(QuestionsMarks("acc?7??sss?3rr1??????5"))         # True
    print(QuestionsMarks("9???1???9??1???9"))               # False
    print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))     # False
    print(QuestionsMarks("9???1???9???1???9"))              # True
    print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5"))  # True


