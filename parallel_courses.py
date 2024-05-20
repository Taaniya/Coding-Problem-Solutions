"""
Problem statement:
Given an integer n, indicating the no. of courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], 
representing a prerequisite relationship between course prevCourse_i and course nextCourse_i: course prevCourse_i has to be taken before course nextCourse_i.
In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.
Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

E.g., Input: n = 3, relations = [[1,3],[2,3]]
Output: 2

Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Since no course can be studied because they are prerequisites of each other.
----------------------------------------------------------------------------------------------------------

Approach: Topological sort with BFS with linear time complexity

Intuition -
The problem statement aligns with that of topological sorting where the linear ordering of graph vertices is such that the order of vertices in 
directed edges retained during traversal.
Here, each vertex represents a course throughout the programme and the set of courses that require no prerequisite courses (or alternatively, 
all prerequisite courses have been completed) represent the next semester to start with.

Approach -
The overall approach follows the flow to perform topological sort in addition to keeping track of no. of semesters (by grouping courses) along the way.
We start with building the DAG with graph in edge list representation from given relations & computing in-degrees of each course to keep track of 
no. of previous courses required to complete as prerequisites.
Courses with 0 in-degrees will represent the 1st semester.
If there is no course found with 0 in-degree, this indicates a cycle in the graph and we return -1 (there's no way to complete the semester).

Beginning with courses of 1st semester, we explore & update in-degrees of next courses as current course gets completed & also update the 
set of courses for semester by including next courses we find during traversal whose in-degree reduces to 0 after completing current semester's course.
We keep traversing the graph until all courses get completed (all vertices are visited)


Time complexity:
V - No. of vertices
E - No. of edges in graph
Initializing in-degree dictionary - O(E)
Initializing set of vertices with in-degree = 0 in beginning = O(V)
During traversal, each vertex is visited atmost once throughout and each semester involves visiting a set of vertices only (those with in-degree 0) 
& decrementing in-degree of their subsequent vertices (next courses). Updating the in-degrees take constant time O(1), hence the time for traversal overall takes O(E) time
Overall time complexity is linear = O(V + E)

Space complexity:
O(N) , where N is the total no. of courses (no. of vertices in graph)
"""

from collections import defaultdict
import copy

class graph:
    def __init__(self) -> None:
        self.graph = defaultdict(set)

    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].add(v)

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:    
        require_no_prev_courses = set()   # in-degree=0, maintain all courses for an ongoing semester
        in_degrees = [0 for _ in range(0, n+1)] # maintain in-degrees for each course
        num_courses_done = 0    
        num_semesters_done = 0
        sem_plan = graph()

        #  compute in-degrees count of each vertex - O(E)
        for rel in relations:
            sem_plan.addEdge(rel[0], rel[1])        # map previous course to next courses``
            in_degrees[rel[1]] += 1
    
        for course, in_degree in enumerate(in_degrees[1:], start=1):
            if in_degree == 0:
                require_no_prev_courses.add(course)
 
        while (num_courses_done != n): # until all courses get completed
            if not len(require_no_prev_courses):
                # If there exists no vertex with 0 in-degree, then there's a cycle
                return -1   

            #  start with vertex with 0 in-degree     
            current_sem_courses = copy.deepcopy(require_no_prev_courses)  # reset course for current sem
            require_no_prev_courses = set()
        
            for course in current_sem_courses:
                for next_course in sem_plan.graph[course]:
                    in_degrees[next_course] -= 1
                    if in_degrees[next_course] == 0:       # no previous courses required anymore
                        require_no_prev_courses.add(next_course)
                num_courses_done += 1
            num_semesters_done += 1
                    
        return num_semesters_done 
            
