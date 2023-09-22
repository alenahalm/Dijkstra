from graph import Graph

connections = {
    1: [(2, 10), (3, 6), (4, 8)],
    2: [(4, 5), (7, 11)],
    3: [(5, 3)],
    4: [(3, 2), (5, 5), (6, 7), (7, 12)],
    5: [(6, 9), (9, 12)],
    6: [(8, 8), (9, 10)],
    7: [(6, 4), (8, 6)],
    8: [(9, 1)],
    9: []
}

gr = Graph(connections)
ds, ps = gr.find_path(1, 9)

D, P = gr.Dijkstra(1)
print(D)
print(P)
# print('Distance', ds)
# print('Path', ps)