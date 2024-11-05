class Graph:
    def __init__(self, adjacency_matrix):
        self.graph = {}
        self.initialize_graph(adjacency_matrix)

    # Initialize the graph with an adjacency matrix
    def initialize_graph(self, adjacency_matrix):
        for vertex_1 in adjacency_matrix:
            self.graph[vertex_1] = []
            for vertex_2, cost in adjacency_matrix[vertex_1].items():
                if cost != float('inf'):  # Skip if there's no direct edge
                    self.graph[vertex_1].append((vertex_2, cost))

    # Print the graph
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} --> {edges}")

    # Print all pairs shortest paths
    def print_all_pairs_shortest_paths(self, distances):
        for vertex, dist in distances.items():
            print(f"Shortest distances from start to {vertex}: {dist}")

    # Floyd-Warshall's algorithm
    def floyd_warshall(self):
        vertices = list(self.graph.keys())
        num_vertices = len(vertices)

        # Create a distance matrix initialized to the adjacency matrix
        distances = {vertex: {v: float('inf') for v in vertices} for vertex in vertices}
        for vertex in vertices:
            distances[vertex][vertex] = 0  # Distance to self is zero
            for neighbor, weight in self.graph[vertex]:
                distances[vertex][neighbor] = weight

        # Update the distances based on the Floyd-Warshall algorithm
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        return distances


# Example usage with adjacency matrix
if __name__ == "__main__":
    # Adjacency matrix represented as a dictionary of dictionaries
    adjacency_matrix = {
    'A': {'B': 4, 'C': 2, 'D': float('inf')},  
    'B': {'C': 1, 'D': 7},                     
    'C': {'D': 3},                             
    'D': {}                                    
}


    new_graph = Graph(adjacency_matrix)

    print("Graph representation:")
    new_graph.print_graph()

    distances = new_graph.floyd_warshall()
    
    print("\nAll pairs shortest distances:")
    new_graph.print_all_pairs_shortest_paths(distances)
