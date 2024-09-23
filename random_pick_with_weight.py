"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. 
The probability of picking an index i is w[i] / sum(w).
For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
"""

import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
      self.w = w
      self.cum_weights = []

      # Compute cumulative freq
      cum_weight = 0
      for weight in self.w:
          cum_weight += weight
          self.cum_weights.append(cum_weight)


    def pickIndex(self) -> int:
      """
      This function basically implements python inbuilt function random. E.g., below -

      class Solution:
        def __init__(self, w: List[int]):
          self.w = w
        
        def pickIndex(self) -> int:
          choices = [i for i in range(len(self.w))]
          return random.choices(choices, weights=self.w, k=1)[0]
      """
      N = random.uniform(0, self.cum_weights[-1])
      return bisect.bisect_left(self.cum_weights, N)


if __name__ == "__main__":
    sol = Solution([1, 3])
    index = sol.pickIndex()
    print(index)


