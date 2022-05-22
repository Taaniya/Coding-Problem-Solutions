#! /bin/user/env python 

def getCount(d, lookup=None):
    """
    Finds the number of ways a distance can be covered by 1,2 and 3 steps.

    Parameters:
    ---------------
    d : (int) distance to be covered
    lookup :(tuple) dictionary containing pairs of distance and number of ways tocover it
    
    Returns:
    ----------
    num_ways : (int)
    
    eg. 
    >> getCount(3)
    >> 4
    
    """
    if lookup is None:
         lookup = dict()

    if d in lookup:
        return lookup[d]

    if d == 0:
        return 1

    if d < 0:
        return 0
    
    if d not in lookup:
        # For every distance of d units, we can take either 1, 2 or 3 steps. 
        # Let's consider all 3 possbilities and sum up the ways in which the 
        # remaining distances can be covered recursively.
        # Similar to a group by dist & aggregate (sum(ways[d] for d in [1,2,3]))
        num_ways = getCount(d - 1, lookup) + getCount(d - 2, lookup) + getCount(d - 3, lookup)
        lookup[d] = num_ways
        return num_ways
    
    
    
# Using LRU cache
from functools import lru_cache

@lru_cache(maxsize=100)
def coverDist(covered, D):
  """ 
  E.g., 
  >> coverDist(0, 4)
  >> 7
  """
  if covered == D:
    return 1
  elif covered > D:
    return 0
  else:  
    count =  coverDist(covered + 1, D) + coverDist(covered + 2, D) + coverDist(covered + 3, D)
  return count



# Using lookup dictionary
lookup = {}

def coverDist(covered, D):
  """
  E.g.,
  >> coverDist(0, 3)
  >> 4
  """
  if lookup.get(covered, None):
    return lookup[covered]
  if covered == D:
    return 1
  elif covered > D:
    return 0
  else:  
    lookup[covered] = coverDist(covered + 1, D) + coverDist(covered + 2, D) + coverDist(covered + 3, D)
  return lookup[covered]
