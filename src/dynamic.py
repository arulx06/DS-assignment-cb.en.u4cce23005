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

    # Print shortest paths from the source to each vertex
    def print_shortest_paths(self, source, distances):
        for vertex, dist in distances.items():
            print(f"Shortest distance from {source} to {vertex}: {dist}")

    # Bellman-Ford algorithm for shortest path from a single source
    def bellman_ford(self, source):
        # Initialize distances from the source
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[source] = 0

        # Relax edges |V| - 1 times
        for _ in range(len(self.graph) - 1):
            for vertex in self.graph:
                for neighbor, weight in self.graph[vertex]:
                    if distances[vertex] != float('inf') and distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight

        # Check for negative-weight cycles
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                if distances[vertex] != float('inf') and distances[vertex] + weight < distances[neighbor]:
                    print("Graph contains a negative-weight cycle")
                    return None

        return distances


# Example usage with adjacency matrix
if __name__ == "__main__":
    # Adjacency matrix represented as a dictionary of dictionaries
    # Example directed graph represented as an adjacency matrix
    adjacency_matrix = {
    'A': {'B': 4, 'C': 1},       
    'B': {'C': -2, 'D': 2},      
    'C': {'D': 3},               
    'D': {'A': 1} 
    }


    new_graph = Graph(adjacency_matrix)

    print("Graph representation:")
    new_graph.print_graph()

    source = 'A'
    distances = new_graph.bellman_ford(source)

    if distances:
        print(f"\nShortest paths from {source}:")
        new_graph.print_shortest_paths(source, distances)
