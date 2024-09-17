"""
Problem statement: 
----------------------------------------------------------------------------------------
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
--------------------------------------------------------------------------------------

Approach -
Gist: Based on sliding window technique with dynamic window size using two pointers to represent window start and end.

The algorithm iterates through the entire string once using right pointer representing the start of the window, while 
maintaining the frequency of characters within the window at any given time.

The window expands if replacing upto characters within the window can lead to a substring within the window containing the same letter throughout. 
This constraint is checked by subtracting the maximum of frequency of characters in given window by the window size.

This indirectly gives us a sense of no. of unique characters within the window.

num_unique_chars = window size - max(freq.values()) + 1
This logic is implemented as in the code.

if window_size - max(freq.values()) <= k:
E.g., ABCD, k=2
for window of size 3, holding substring 'ABC', max freq = 1
since each char A, B, C are present only once.
hence, in this case,

num_unique_chars = 3 - 1 + 1 = 3
As long as the num_unique_chars - 1 is <= K, we replace any 2 chars with the 3 char in this window to obtain a substring of size 3 with same letter. 
E.g., AAA or BBB or CCC

However, next let's suppose window moves further, start index incremenets to have 'ABCD' in window, to result -

num_unique_chars = 4 - 1 + 1 = 4
Since only upto K = 2 chars can be replaced, this won't result in a substring of same letter. Hence, since this constraint is violated, 
we reduce the window size by 1 (incrementing window end by 1 to move ahead) to keep the no. of unique chars for replacement within the available constraint k.

Complexity
Time complexity:
O(n)

Space complexity:
O(n)
worst case - when all characters in string are unique, & k = n, where len(freq) = n. 
   E.g., s = "ABCD" , K = 4
best case - when k=1, or all characters in string are same already, where len(freq) = 1
   E.g., s = "AAAA" , K = any value
         s = ABCD, K = 1  
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_end = 0
        freq = {}
        maxlen = 0
        for window_start in range(len(s)):
            freq[s[window_start]] = freq.get(s[window_start], 0) + 1

            window_size = window_start - window_end + 1       # current length of substring
            if window_size - max(freq.values()) <= k:     
                maxlen = max(maxlen, window_size)
            else:
                # reduce window size by 1 when too many unique chars are present 
                # than K replacements constraint allows
                freq[s[window_end]] -= 1      # increment end pointer to reduce window size by 1
                window_end += 1

        return maxlen
