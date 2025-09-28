from kb_loader import load_stations, load_edges, load_rules
from search import find_best_route
import os, json

def run_tests():
    base = os.path.join(os.path.dirname(__file__), '..', 'data')
    stations = load_stations(os.path.join(base, 'stations.json'))
    edges = load_edges(os.path.join(base, 'edges.json'))
    rules = load_rules(os.path.join(base, 'rules.json'))

    scenarios = [
        ("PN", "C85", False),
        ("P80", "C85", False),
        ("PS", "C85", False),
        ("P80", "C85", True)  # hora pico
    ]

    for s,g,peak in scenarios:
        r = find_best_route(s, g, edges, rules, peak=peak)
        print(f"Prueba {s} -> {g} (peak={peak}):")
        if r:
            print("  Costo:", round(r['cost'],2))
            print("  Ruta:", " -> ".join(r['path']))
        else:
            print("  SIN RUTA (restricciones)")

if __name__ == '__main__':
    run_tests()