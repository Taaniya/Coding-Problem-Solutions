#! /usr/bin/env python
"""
Problem statement -
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, 
returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies 
the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed 
since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair 
represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that 
represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

Assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability 
don’t overlap. Further assume that the slots are sorted by slots’ start time.

Time complexity - O(m + n). Linear time. Time slots for both A & B are processed atmost once.
Space complexity - O(1). Uses constant space
"""

from typing import List, Any, Tuple

def meeting_planner(slotsA: List[List[int]] , slotsB: List[List[int]], dur: int) -> List[Any]:
  """
  E.g., 
  >> meeting_planner([[7,12]], [[2,11]], 5)
  >> []
  >> meeting_planner([[6,12]], [[2,11]], 5)
  >> [6,11]
  >> meeting_planner([[1,10]], [[2,3],[5,7]], 2)
  >> [5,7]
  >> meeting_planner([[0,5],[50,70],[120,125]], [[0,50]], 8)
  >> []
  >> meeting_planner([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)
  >> [60, 68]
  >> meeting_planner([[10,50],[60,120],[140,210]], [[0,15],[60,72]], 12)
  >> [60, 72]
  """
  i_a = 0
  i_b = 0
  start = 0

  while i_a < len(slotsA) and i_b < len(slotsB):
    start = max(slotsA[i_a][0], slotsB[i_b][0])
	
    if start >= slotsA[i_a][1]:
      i_a += 1
      continue
    elif start >= slotsB[i_b][1]:
      i_b += 1
      continue
    
    end = start + dur     
    
    if end > slotsA[i_a][1]:
      i_a += 1
      continue
	
    if end > slotsB[i_b][1]:
      i_b += 1
      continue

    if (end <= slotsA[i_a][1]) and (end <= slotsB[i_b][1]):
       return [start, end]
      
  return []

# Alternative approach with same time complexity
def meet_planner(slotsA: List[Tuple[int, int]], slotsB:List[Tuple[int, int]], dur: int) -> Any:
    ia = 0
    ib = 0
  
    while((ia < len(slotsA)) & (ib < len(slotsB))):  
      if slotsA[ia][1] - slotsA[ia][0] < dur:
        ia += 1
        print(f"inside if ia {ia}")
        continue
      if slotsB[ib][1] - slotsB[ib][0] < dur:
        ib += 1
        continue
      
      # check whether availability of both satisfies the duration constraint
      if slotsB[ib][0] <= slotsA[ia][0]:                  # if B is available before A
        # ensure B's availability ends atleast 'dur' seconds after A's starts
        if (slotsB[ib][1] - slotsA[ia][0] >= dur):        
          start = max(slotsA[ia][0], slotsB[ib][0])
          return [start, start + dur]
        else:
          ib += 1
      else:
        if (slotsA[ia][1] - slotsB[ib][0] >= dur):
          start = max(slotsA[ia][0], slotsB[ib][0])
          return [start, start + dur]
        else:
          ia += 1
    return []

if __name__ == "__main__":
  print(meeting_planner([[1,10]], [[2,3], [5,7]], 2))
  
  
