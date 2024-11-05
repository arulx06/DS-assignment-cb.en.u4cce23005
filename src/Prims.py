import heapq

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

    # Prim's algorithm for Minimum Spanning Tree
    def prim_mst(self, start_vertex):
        mst_cost = 0
        visited = set()
        min_heap = [(0, start_vertex)]  # (cost, vertex)
        mst_edges = []

        while min_heap:
            current_cost, current_vertex = heapq.heappop(min_heap)
            
            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            mst_cost += current_cost
            
            if current_cost != 0:
                mst_edges.append((current_vertex, current_cost))

            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

        return mst_cost, mst_edges

# Example usage with adjacency matrix
if __name__ == "__main__":
    adjacency_matrix = {
        'A': {'B': 4, 'C': 2, 'D': float('inf')},
        'B': {'A': 4, 'C': 1, 'D': 7},
        'C': {'A': 2, 'B': 1, 'D': 3},
        'D': {'B': 7, 'C': 3}
    }

    new_graph = Graph(adjacency_matrix)

    print("Graph representation:")
    new_graph.print_graph()

    start_vertex = 'A'
    mst_cost, mst_edges = new_graph.prim_mst(start_vertex)

    print(f"\nTotal cost of MST by Prim's Algorithm starting from '{start_vertex}': {mst_cost}")
    print("Edges in the MST:", mst_edges)
