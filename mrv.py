import random


def mrv(graph, colors):
    key = list(graph)[0]
    node = graph[key]
    assigned = 0
    visited = set()

    while True:
        node['color'] = random.choice(node['values'])
        assigned += 1
        visited.add(key)

        if assigned == len(graph):
            break

        # shrink neighbours' domain

        for neighbour in node['neighbours']:

            if neighbour not in visited:
                neighbour_domain = graph[neighbour]['values']
                try:
                    neighbour_domain.remove(node['color'])
                except ValueError:
                    pass

        mini = len(colors) + 1

        for k, item in graph.items():

            if k in visited:
                continue

            r = len(item['values'])
            if r < mini:
                mini = r
                node = item
                key = k

def test(graph):

    if graph['Balochistan']['color'] == graph['Sindh']['color'] or graph['Balochistan']['color'] == graph['Punjab'][
        'color'] or graph['Balochistan']['color'] == graph['NWFP']['color'] or graph['Sindh']['color'] == \
         graph['Punjab']['color'] or graph['NWFP']['color'] == graph['Punjab']['color'] or graph['Punjab']['color'] == graph['Kashmir']['color'] or graph['NWFP']['color'] == graph['Kashmir']['color']:

        print("Failed")

    else:
        print("Passed")


if __name__ == "__main__":

    domain = ['red', 'green', 'blue']

    graph = {
        'Balochistan': {'neighbours': ['Sindh', 'Punjab', 'NWFP'], 'values': domain[:]},
        'Sindh': {'neighbours': ['Balochistan', 'Punjab'], 'values': domain[:]},
        'Punjab': {'neighbours': ['Sindh', 'Punjab', 'NWFP', 'Kashmir'], 'values': domain[:]},
        'NWFP': {'neighbours': ['Punjab', 'Balochistan', 'Kashmir'], 'values': domain[:]},
        'Kashmir': {'neighbours': ['NWFP', 'Punjab'], 'values': domain[:], 'color': ""}
    }
    mrv(graph, domain)
    for k, item in graph.items():
        print(k + ":" + item['color'])

    test(graph)



