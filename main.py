from queue import PriorityQueue
dict1={'A':1, 'B':2, 'C':3, 'E':5, 'F':6, 'G':7}
#open set which is a priority queue is the frontier ie predicts which node to expand to next

def weight(seat):
    global dict1
    return (dict1[seat[0]] + int(seat[1]))

def distance(node1,node2):
    global dict1
    return abs(dict1[node1[0]]-dict1[node2[0]]) + abs(int(node1[1])-int(node2[1]))

def heuristic(node1,node2):
    #return(distance(start,node1) + distance(node1,node2))
    return distance(node1,node2)

def astar(start, goal, graph):
    # Initialize open and closed sets
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float("inf") for node in graph} # cost function
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph} # heuristic
    f_score[start] = heuristic(start, goal)
    visited=[]

    while not open_set.empty():
        # Get node with lowest f_score
        current = open_set.get()[1]
        visited.append(current)

        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            print("visited :", visited)
            print("Frontier: ",open_set.queue)
            return path


        # Generate neighbors
        for neighbor in graph[current]:
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + distance(current, neighbor)
            tentative_f_score = tentative_g_score + heuristic(neighbor, goal)

            if tentative_f_score < f_score[neighbor]:
                # This path to neighbor is better than any previous one
                came_from[neighbor] = current
                g_score[neighbor] = g_score[current] + distance(current, neighbor) # updates the cost function
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set.queue:
                    open_set.put((f_score[neighbor], neighbor))

    # No path found
    return None



# Example usage:
graph = {
    'A1': ['B1','A2' ],
    'A2': ['A1','A3' ],
    'A3': ['A2','B3' ],
    'B1': ['A1','C1' ],
    'B2': [],
    'B3': ['B4','A3','C3'],
    'C1': ['B1','E1','C2' ],
    'C2': ['E2','C3'],
    'C3': ['C4','B3','C2' ],
    'C4': ['B4','C5','C3' ],
    'E1': ['C1','F1','E2'],
    'E2': ['E1','C2' ],
    'E3': [],
    'F1': ['E1','G1' ],
    'F2': [],
    'F3': ['F4',],
    'G1': ['F1','G2' ],
    'G2': ['G1',],
    'G3': [],
    'A4': [],
    'A5': ['A6',],
    'A6': ['B6','A5'],
    'B4': ['C4','B3'],
    'B5': [],
    'B6': ['A6','C6'],
    'C5': ['E5','C4','C6'],
    'C6': ['B6','C5' ],
    'E4': [],
    'E5': ['F5','C5' ],
    'E6': [],
    'F4': ['F3','G4' ],
    'F5': ['F4','F6','E5','G5'],
    'F6': ['F5','G6'],
    'G4': ['F4','G5' ],
    'G5': ['G4','F5','G6'],
    'G6': ['G5','F6']

}

start = 'G2'
goal = 'G6'
path = astar(start, goal, graph)
print(path)  # Output: ['A', 'B', 'E', 'H']
