class Graph: 
    def __init__(self, num_vertices): 
        self.num_vertices = num_vertices 
        # Initialize adjacency matrix with None for no direct edge 
        self.graph = [[None] * num_vertices for _ in range(num_vertices)] 
  
    # Method to add a directed, weighted edge to the graph 
    def add_edge(self, u, v, weight): 
        self.graph[u][v] = weight  # Only one direction for directed graph 
  
    def bfs(self, start_vertex): 
        visited = set()  # Set to keep track of visited nodes 
        queue = [start_vertex]  # Queue to support BFS traversal 
        bfs_result = [] 
  
        while queue: 
            vertex = queue.pop(0) 
            if vertex not in visited: 
                visited.add(vertex) 
                bfs_result.append(vertex) 
  
                # Add all unvisited neighbors to the queue 
                for neighbor in range(self.num_vertices): 
                    # Check for a valid edge and if neighbor is unvisited 
                    if self.graph[vertex][neighbor] is not None and neighbor not in visited: 
                        queue.append(neighbor) 
  
        return bfs_result 
  
    def dfs(self, start_vertex): 
        visited = set()  # Set to keep track of visited nodes 
        stack = [start_vertex]  # Stack to support DFS traversal 
        dfs_result = [] 
  
        while stack: 
            vertex = stack.pop() 
            if vertex not in visited: 
                visited.add(vertex) 
                dfs_result.append(vertex) 
  
                # Add all unvisited neighbors to the stack 
                for neighbor in range(self.num_vertices - 1, -1, -1):  # Reverse order to maintain stack behavior 
                    if self.graph[vertex][neighbor] is not None and neighbor not in visited: 
                        stack.append(neighbor) 
  
        return dfs_result 
  
if __name__ == "__main__": 
    num_vertices = 4  # 0, 1, 2, 3 
    g = Graph(num_vertices) 
     
    # Adding directed, weighted edges to the graph 
    edges = [ 
        (0, 1, 3),   # Edge from 0 to 1 with weight 3 
        (0, 2, 1),   # Edge from 0 to 2 with weight 1 
        (1, 3, 2),   # Edge from 1 to 3 with weight 2 
        (2, 3, 1)    # Edge from 2 to 3 with weight 1 
    ] 

    for u, v, weight in edges: 
        g.add_edge(u, v, weight) 
        
    print("Breadth First Search (starting from vertex 0):", g.bfs(0)) 
    print("Depth First Search (starting from vertex 0):", g.dfs(0))
