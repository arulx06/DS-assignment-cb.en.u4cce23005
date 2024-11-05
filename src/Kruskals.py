class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

class Graph:
    def __init__(self, adjacency_matrix):
        self.edges = []
        self.vertices = list(adjacency_matrix.keys())
        self.initialize_graph(adjacency_matrix)

    # Initialize edges from the adjacency matrix
    def initialize_graph(self, adjacency_matrix):
        for vertex_1 in adjacency_matrix:
            for vertex_2, cost in adjacency_matrix[vertex_1].items():
                if cost != float('inf') and (vertex_2, vertex_1, cost) not in self.edges:
                    self.edges.append((vertex_1, vertex_2, cost))

    # Print the graph edges
    def print_edges(self):
        for edge in self.edges:
            print(f"{edge[0]} --({edge[2]})--> {edge[1]}")

    # Kruskal's algorithm for Minimum Spanning Tree
    def kruskal_mst(self):
        # Sort edges by weight
        self.edges.sort(key=lambda edge: edge[2])

        union_find = UnionFind(self.vertices)
        mst_cost = 0
        mst_edges = []

        for u, v, weight in self.edges:
            if union_find.union(u, v):
                mst_cost += weight
                mst_edges.append((u, v, weight))

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

    print("Graph edges:")
    new_graph.print_edges()

    mst_cost, mst_edges = new_graph.kruskal_mst()

    print(f"\nTotal cost of MST by Kruskal's Algorithm: {mst_cost}")
    print("Edges in the MST:", mst_edges)
