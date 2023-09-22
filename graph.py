from collections import defaultdict

class Node:
    def __init__(self, name, neighbours=[]) -> None: # neighbours is a list of tuples: [(name, weight)]
        self.name = name
        self.neighbours = neighbours
    
    def get_name(self):
        return self.name
    
    def get_neighbours(self):
        return self.neighbours

    def add_neighbour(self, neighbour, w): # neighbour is string
        self.neighbours.append((neighbour, w))

    def remove_neighbour(self, neighbour):
        for n, w in self.neighbours:
            if n == neighbour:
                self.neighbours.remove((n, w))
                break

class Graph:
    def __init__(self, connections) -> None: # get list of nodes from dict of connetions
        self.nodes = []
        for n in connections.keys():
            self.nodes.append(Node(n, connections[n]))
    
    def get_node_by_name(self, name) -> Node:
        for n in self.nodes:
            if n.get_name() == name:
                return n
    
    def Dijkstra(self, start):
        D = {}
        V = {}
        P = {}
        for n in self.nodes:
            D[n.get_name()] = 10000
            V[n.get_name()] = False
            P[n.get_name()] = None
        D[start] = 0
        
        for n in self.nodes:
            for key in D.keys():
                if not V[key]:
                    cur_min_node = key
                    break
            for key in D.keys():
                if not V[key]:
                    if D[cur_min_node] > D[key]:
                        cur_min_node = key

            V[cur_min_node] = True
            node = self.get_node_by_name(cur_min_node)

            for to, weight in node.get_neighbours():
                if D[to] > D[cur_min_node] + weight:
                    D[to] = D[cur_min_node] + weight
                    P[to] = cur_min_node
        return D, P
    
    def find_path(self, start, finish):
        D, P = self.Dijkstra(start)
        cur_point = finish
        path = []
        while cur_point != start:
            path.append(cur_point)
            cur_point = P[cur_point]
        path.append(start)
        path.reverse()
        return D[finish], path