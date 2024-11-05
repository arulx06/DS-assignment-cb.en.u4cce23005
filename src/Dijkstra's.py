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

    # Print distances
    def print_distances(self, distances):
        for vertex, distance in distances.items():
            print(f"Distance from start to {vertex} is {distance}")

    # Min-Heap Implementation without using heapq
    class MinHeap:
        def __init__(self):
            self.heap = []

        def push(self, element):
            self.heap.append(element)
            self._heapify_up(len(self.heap) - 1)

        def pop(self):
            if len(self.heap) == 0:
                return None
            self._swap(0, len(self.heap) - 1)
            min_element = self.heap.pop()
            self._heapify_down(0)
            return min_element

        def _heapify_up(self, index):
            parent_index = (index - 1) // 2
            if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
                self._swap(index, parent_index)
                self._heapify_up(parent_index)

        def _heapify_down(self, index):
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
                smallest = right_child

            if smallest != index:
                self._swap(index, smallest)
                self._heapify_down(smallest)

        def _swap(self, i, j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        def is_empty(self):
            return len(self.heap) == 0

    # Dijkstra's algorithm
    def dijkstra(self, start):
        min_heap = self.MinHeap()
        min_heap.push((0, start))  # (distance, vertex)
        distances = {vertex: float("infinity") for vertex in self.graph}
        distances[start] = 0
        visited = set()  # To track visited vertices

        while not min_heap.is_empty():
            current_distance, current_vertex = min_heap.pop()

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            # Explore all neighbors of the current vertex
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    min_heap.push((distance, neighbor))

        # Find unvisited vertices (unreachable vertices)
        unreachable = [vertex for vertex in self.graph if vertex not in visited]

        return distances, unreachable


# Example usage with adjacency matrix
if __name__ == "__main__":
    # Adjacency matrix represented as a dictionary of dictionaries with alphabetic legends
    adjacency_matrix = {
    'A': {'B': 4, 'C': 2, 'D': float('inf')},  # A -> B (4), A -> C (2), A -> D (no edge)
    'B': {'C': 1, 'D': 7},                     # B -> C (1), B -> D (7)
    'C': {'D': 3},                             # C -> D (3)
    'D': {}                                     # D has no outgoing edges
}


    new_graph = Graph(adjacency_matrix)

    print("Graph representation:")
    new_graph.print_graph()

    start_vertex = 'A'
    distances, unreachable = new_graph.dijkstra(start_vertex)
    
    print("\nShortest distances from source vertex:")
    new_graph.print_distances(distances)
    print("\nUnreachable vertices:", unreachable)
