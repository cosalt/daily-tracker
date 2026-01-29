"""
Overview:
    find the bomb that has the 
        highest number of bombs in its range
        chain of bombs are allowed (explode bomb outside its range but in connected range)



Inputs:
    2D Array: bombs[i] = [xi, yi, ri]
        x_i, y_i = coord on graph
        r_i = radius

Outputs:
    int: number of explosions

notes:
    this is a directed graph with no root, then find the node with the highest weight
    inside radius if: 
        (x - center_x)² + (y - center_y)² < radius²
            x - center_x → horizontal distance from the point to the circle center
            y - center_y → vertical distance from the point to the circle center
            Squaring them → A^2 + B^2 represents the squared distance from the point to the circle center
            < radius² → if the squared distance is less than the squared radius, the point is inside the circle

Build graph:

"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ### Stage 1: Build Graph
        # Checks if bomb is with radius
        def inBombRange(bomb, point):
            centreX, centreY, radius = bomb
            pointX, pointY = point
            return ((pointX - centreX)**2 + (pointY - centreY)**2 <= radius**2)

        def buildGraph():
            # initialise directed graph nodes
            graph = {i:[] for i in range(len(bombs))}

            for i in range(len(bombs)): # for every bomb
                for j in range(len(bombs)): # for every point
                    # check if point in bomb range (dont check bomb against itself)
                    if i != j and inBombRange(bombs[i], bombs[j][:2]):
                        graph[i].append(j) # append directed edge to node
            return graph

        graph = buildGraph()

        ### Stage 2: DFS graph

        def DFS(node, visited):
            if node in visited: return 0

            visited.add(node)
            explosionCount = 1

            for subNode in graph[node]: # branch traversal
                if subNode not in visited:
                    explosionCount += DFS(subNode, visited)
            
            return explosionCount
        

        maxExplosions = 0

        for i in range(len(bombs)):
            visited = set()
            maxExplosions = max(maxExplosions, DFS(i, visited))

        return maxExplosions
            





