def a_star(start, goal, obstacles):
    open_set = [start]
    came_from = {}
    cost = {start: 0}

    while open_set:
        current = open_set.pop(0)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            if neighbor in obstacles:
                continue
            new_cost = cost[current] + 1
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                open_set.append(neighbor)
                came_from[neighbor] = current

    return None  # No path found

def get_neighbors(node):
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
