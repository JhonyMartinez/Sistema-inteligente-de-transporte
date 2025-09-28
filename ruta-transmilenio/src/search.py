import heapq
from typing import List, Dict, Any
from engine import apply_rules_to_edge

def build_adj(edges: List[Dict]) -> Dict[str, List[Dict]]:
    adj = {}
    for e in edges:
        u, v = e['from'], e['to']
        adj.setdefault(u, []).append(e)
        # crear arista inversa (suponiendo simetría)
        rev = dict(e)
        rev['from'], rev['to'] = v, u
        adj.setdefault(v, []).append(rev)
    return adj

def find_best_route(start: str, goal: str, edges: List[Dict], rules: Dict, peak: bool=False):
    adj = build_adj(edges)
    pq = []
    # (cost, node, prev_line, path)
    heapq.heappush(pq, (0.0, start, None, [start]))
    visited = {}  # (node, prev_line) -> best cost

    while pq:
        cost, node, prev_line, path = heapq.heappop(pq)
        if node == goal:
            return {'cost': cost, 'path': path}

        key = (node, prev_line)
        if key in visited and visited[key] <= cost:
            continue
        visited[key] = cost

        for edge in adj.get(node, []):
            next_node = edge['to']
            edge_line = edge.get('line')
            transfer = False
            if prev_line is not None and edge_line != prev_line:
                transfer = True

            state = {'transfer': transfer, 'peak': peak}
            effective = apply_rules_to_edge(edge, rules, state)
            if effective == float('inf'):
                continue
            new_cost = cost + effective
            heapq.heappush(pq, (new_cost, next_node, edge_line, path + [next_node]))

    return None