import heapq

# Ek simple grid jahan 0 matlab rasta saaf hai, aur 1 matlab deewar/rukawat hai
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_node = (0, 0) # Shuruwat (Top-Left)
end_node = (4, 4)   # Manzil (Bottom-Right)

# Heuristic function (Manhattan distance calculation)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search Algorithm Logic
def a_star_search(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        current_f, current = heapq.heappop(open_list)
        
        # Agar manzil mil gayi
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Padosi nodes (Up, Down, Left, Right)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dy, dx in neighbors:
            neighbor = (current[0] + dy, current[1] + dx)
            
            # Check grid boundaries aur rukawat (1)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_score, neighbor))
                    
    return "Rasta nahi mila!"

# Run the Algorithm
print("--- Algorithmic Pathfinding (A* Search) ---")
print(f"Start Point: {start_node}")
print(f"End Point: {end_node}")
print("\nGrid Map (0=Clear, 1=Obstacle):")
for row in grid:
    print(row)

optimal_path = a_star_search(grid, start_node, end_node)

print(f"\nOptimal Path Found: {optimal_path}")
print(f"Total Steps: {len(optimal_path) - 1}")