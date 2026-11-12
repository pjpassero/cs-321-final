import heapq

grid =  [
     [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


start = (0,0)
goal = (4,4)


#heuristic  with Manhattan Distance:  h(n) = |x1 - x2| + |y1 - y2|
#f(n) = g(n) + h(n)


def heuristic(a,b):
    return abs(a[0] - b[0]) + abs(a[1]-b[1])


def astar(grid, start, goal):
    open_set = [] #nodes that are waitng to be explored
    heapq.heappush(open_set, (0,start)) #add the node to the priority queue
    came_from = {}#keep track of where each node came from so we can reconstruct the path
    g_score = {start:0} #shortest distance discovered from start to each node

    while open_set:
        current_f, current = heapq.heappop(open_set)

        #if we reach the goal, we want to construct the path
        if(current == goal):
            print("Goal Achieved!")
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()

            return path
        #directions that we can move: right, left, up, down (not in that order)
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        #check the neighbor and calculate the next place we want to go that is valid, ie no blockages or walls
        for dr, dc in directions:
            neighbor = (current[0]+dr, current[1]+dc)
            if (
                0 <= neighbor[0] < len(grid)
                and 0 <= neighbor[1] < len(grid[0])
                and grid[neighbor[0]][neighbor[1]] == 0
            ):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f_score = tentative_g + heuristic(neighbor, goal)

                    heapq.heappush(open_set, (f_score, neighbor))

path = astar(grid, start, goal)

print("Shortest Path: ", path)