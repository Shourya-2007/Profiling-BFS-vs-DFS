import timeit
from collections import deque

# ----------------------------------------------------------------------
# Graph Generation (100 Nodes)
# ----------------------------------------------------------------------
NUM_NODES = 100
graph = {}

# Har node ko aane wale nodes se connect karna (Sequential Adjacency)
for i in range(NUM_NODES):
    graph[i] = []
    for j in range(1, 5):
        if i + j < NUM_NODES:
            graph[i].append(i + j)

# ----------------------------------------------------------------------
# BFS Algorithm with Node Counter
# ----------------------------------------------------------------------
def bfs(start_node, goal_node):
    queue = deque([start_node])
    visited = {start_node}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal_node:
            return True, nodes_expanded

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, nodes_expanded

# ----------------------------------------------------------------------
# DFS Algorithm with Node Counter
# ----------------------------------------------------------------------
def dfs(start_node, goal_node):
    stack = [start_node]
    visited = {start_node}
    nodes_expanded = 0

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current == goal_node:
            return True, nodes_expanded

        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False, nodes_expanded

# ----------------------------------------------------------------------
# Profiling Helper Function using timeit
# ----------------------------------------------------------------------
def profile_algorithm(algo_func, start_node, goal_node, runs=3):
    total_time_ms = 0.0
    nodes_expanded = 0
    found = False

    for _ in range(runs):
        # Timeit execution time measurement in milliseconds
        timer = timeit.Timer(lambda: algo_func(start_node, goal_node))
        exec_time_sec = timer.timeit(number=1)
        total_time_ms += exec_time_sec * 1000.0
        
        # Node count execution
        found, nodes_expanded = algo_func(start_node, goal_node)

    avg_time_ms = total_time_ms / runs
    return avg_time_ms, nodes_expanded, found

# ----------------------------------------------------------------------
# Main Execution and Profiling Output
# ----------------------------------------------------------------------
if __name__ == "__main__":
    cases = [
        ("Best", 1),
        ("Average", 50),
        ("Worst", 99)
    ]

    print("======================================================================")
    print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS (Shourya Morbale - 25UAM051)")
    print("======================================================================\n")

    for case_name, goal in cases:
        bfs_time, bfs_nodes, bfs_found = profile_algorithm(bfs, 0, goal)
        dfs_time, dfs_nodes, dfs_found = profile_algorithm(dfs, 0, goal)

        better_time = "DFS" if dfs_time < bfs_time else "BFS"
        
        print(f"--- Case: {case_name} (Start: 0, Goal: {goal}) ---")
        print(f"BFS -> Avg Time: {bfs_time:.5f} ms | Nodes Expanded: {bfs_nodes} | Goal Found: {bfs_found}")
        print(f"DFS -> Avg Time: {dfs_time:.5f} ms | Nodes Expanded: {dfs_nodes} | Goal Found: {dfs_found}")
        print(f"Better in Execution Time: {better_time}\n")