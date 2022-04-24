'''
Give a list of project dependencies (pairs of projects where the 
first project must be built before the second), determine a build order 
that allows all the projects to be built. 

NOTE: This problem is topological sort.

Input:  projects[a, b, c, d, e, f]
        dependencies[(a, d), (f, b), (b, d), (f, a), (d, c)]
Output: f, e, a, b, d, c

Solutions:

##### 1
Repeat until all projects have been processed:
  Move all projects with no dependencies to the build order.
  Remove the incoming edges from projects dependent on moved projects.

'''