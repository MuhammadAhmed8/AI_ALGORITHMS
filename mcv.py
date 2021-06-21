import random

def get_item_having_max_degree(graph, visited):
    maxi = -1

    key = ""
    for k, item in graph.items():
        if k in visited:
            continue
        edges = item['neighbours']
        n = len(edges)
        if n > maxi:
            maxi = n
            key = k

    return key

def mcv(graph, colors):
    assigned = 0
    visited = set()

    while True:
        key = get_item_having_max_degree(graph, visited)

        node = graph[key]

        node['color'] = random.choice(node['values'])

        assigned += 1
        visited.add(key)

        if assigned == len(graph):
            break

        for neighbour in node['neighbours']:

            if neighbour not in visited:
                neighbour_domain = graph[neighbour]['values']
                try:
                    neighbour_domain.remove(node['color'])
                except ValueError:
                    pass


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
        'Punjab': {'neighbours': ['Sindh', 'Balochistan', 'NWFP', 'Kashmir'], 'values': domain[:]},
        'NWFP': {'neighbours': ['Punjab', 'Balochistan', 'Kashmir'], 'values': domain[:]},
        'Kashmir': {'neighbours': ['NWFP', 'Punjab'], 'values': domain[:]}
    }
    mcv(graph, domain)

    for k,item in graph.items():
        print(k + ":" + item['color'])

    test(graph)