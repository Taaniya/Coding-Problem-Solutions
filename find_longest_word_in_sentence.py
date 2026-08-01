"""
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""

import re
from collections import defaultdict

def LongestWord(sen):
  
  

  # if a length is largest among all, return the 1st word from that list
  max_len = 0

  words = sen.split(" ")         # separate by space
  w_len_map = defaultdict(list)
  cleaned_words = [re.sub(r"[^a-zA-Z0-9]","", word) for word in words]

  # create mapping of length & list of words corresponding to that length
  for word in cleaned_words:
    w_len = len(word)
    w_len_map[w_len].append(word)
    if w_len > max_len:
      max_len = w_len
  
  return w_len_map[max_len][0]


if __name__ == "__main__":
  print(LongestWord("fun&!! time"))     # time
  print(LongestWord("I love dogs"))       # love

