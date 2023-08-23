####################### Tarea2 #######################

# input:
#         graph   Represents a graph for the maximum flow problem.
#                 Args:
#                     capacity_matrix (list of list of int): The capacity matrix representing the flow network.
#                         Each entry capacity_matrix[u][v] represents the capacity of the edge from vertex u to vertex v.
#
#                 Attributes:
#                     capacity_matrix (list of list of int): The capacity matrix representing the flow network.
#                         Each entry capacity_matrix[u][v] represents the capacity of the edge from vertex u to vertex v.
#                     n (int): The number of vertices in the graph.
#                     flow_matrix (list of list of int): The flow matrix representing the current flow in the graph.
#                         Each entry flow_matrix[u][v] represents the flow along the edge from vertex u to vertex v.
#         s       (Source vertex)
#         t       (Sink vertex)
#         n       (Number of vertices)
#     output:
#         flow    (Value of maximum flow)

import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, capacity_matrix):
        self.capacity_matrix = capacity_matrix
        self.n = len(capacity_matrix)
        self.flow_matrix = [[0] * self.n for _ in range(self.n)]
        
    def add_edge(self, u, v, capacity):
        self.capacity_matrix[u][v] = capacity
        
def bfs(n, s, t, graph):
    """
    Perform Breadth-First Search (BFS) to find augmenting paths in the residual graph.

    Args:
        n (int): Number of vertices.
        s (int): Source vertex.
        t (int): Sink vertex.
        graph (Graph): Flow network graph.

    Returns:
        list or None: List of edges in the augmenting path, or None if no path exists.
    """
    queue = [s]
    paths = {s: []}
    
    if s == t:
        return paths[s]
    
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if (graph.capacity_matrix[u][v] - graph.flow_matrix[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                print(paths)
                if v == t:
                    return paths[v]
                queue.append(v)
                
    return None

def edmonds_karp(graph, s, t, n):
    """
    Edmonds-Karp algorithm to find the maximum flow in a flow network.

    Args:
        graph (Graph): Flow network graph.
        s (int): Source vertex.
        t (int): Sink vertex.
        n (int): Number of vertices.

    Returns:
        int: Value of the maximum flow in the flow network.
    """
    path = bfs(n, s, t, graph)
    while path:
        flow = min(graph.capacity_matrix[u][v] - graph.flow_matrix[u][v] for u, v in path)
        for u, v in path:
            graph.flow_matrix[u][v] += flow
            graph.flow_matrix[v][u] -= flow
        path = bfs(n, s, t, graph)
    
    return sum(graph.flow_matrix[s][i] for i in range(n))


def read_input_file(filename):
    """
    Read input from the specified file.

    Args:
        filename (str): Path to the input file.

    Returns:
        tuple: Number of vertices and the capacity matrix.
    """
    with open(filename, 'r') as f:
        n = int(f.readline())
        capacity_matrix = [[0] * n for _ in range(n)]
        while True:
            line = f.readline().strip()
            if not line:
                break
            u, v, capacity = map(int, line.split())
            capacity_matrix[u][v] = capacity
        return n, capacity_matrix

def write_output_file(filename, max_flow_value, flow_matrix):
    """
    Write output to the specified file.

    Args:
        filename (str): Path to the output file.
        max_flow_value (int): Value of the maximum flow.
        flow_matrix (list): Flow matrix of the graph.
    """
    with open(filename, 'w') as f:
        f.write("Max flow value: {}\n".format(max_flow_value))
        for u in range(len(flow_matrix)):
            for v in range(len(flow_matrix[u])):
                if flow_matrix[u][v] > 0:
                    f.write("Flow from node {} to node {}: {}\n".format(u, v, flow_matrix[u][v]))

def visualize_graph(graph, flow_matrix, source, sink):
    G = nx.DiGraph()
    n = graph.n

    for u in range(n):
        for v in range(n):
            capacity = graph.capacity_matrix[u][v]
            flow = flow_matrix[u][v]
            if flow > 0 or capacity > 0:
                G.add_edge(u, v, capacity=capacity, flow=flow)

    k_value = 0.4  # Adjust this value for desired node spacing
    pos = nx.spring_layout(G, pos={source: (-k_value, 0), sink: (k_value, 0)}, fixed=[source, sink], k=k_value)
    labels = {(u, v): f"{flow}/{capacity}" for u, v, data in G.edges(data=True) for flow, capacity in [(data['flow'], data['capacity'])]}
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title("Flow Network with Maximum Flow")
    plt.show()

if __name__ == '__main__':
    
    try:
        file_path = sys.argv[1]
        n, capacity_matrix = read_input_file(file_path)
        source = 0
        sink = n - 1

        graph = Graph(capacity_matrix)
        max_flow_value = edmonds_karp(graph, source, sink, n)
        print("Edmonds-Karp algorithm")
        print("max_flow_value is:", max_flow_value)

        output_filename = "output.txt"
        write_output_file(output_filename, max_flow_value, graph.flow_matrix)
        visualize_graph(graph, graph.flow_matrix, source, sink)

    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)


# --------------------------------------------------

# Para pruebas sin el archivo

# # Capacity graph
# C = [[0, 3, 3, 0, 0, 0],
#      [0, 0, 2, 3, 0, 0],
#      [0, 0, 0, 0, 2, 0],
#      [0, 0, 0, 0, 4, 2],
#      [0, 0, 0, 0, 0, 2],
#      [0, 0, 0, 0, 0, 3]]

# source = 0
# sink = 5

# graph = Graph(C)
# max_flow_value = edmonds_karp(graph, source, sink, graph.n)

# print("Edmonds-Karp algorithm")
# print("max_flow_value is:", max_flow_value)