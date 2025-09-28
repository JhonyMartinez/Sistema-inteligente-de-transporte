import argparse
from kb_loader import load_stations, load_edges, load_rules
from search import find_best_route
import os

def cli():
    parser = argparse.ArgumentParser(description="Ruta inteligente (simulación TransMilenio)")
    parser.add_argument('--start', required=True, help="ID estación inicio (ej: PN)")
    parser.add_argument('--goal', required=True, help="ID estación destino (ej: C100)")
    parser.add_argument('--data-dir', default='../data', help="Carpeta con data")
    parser.add_argument('--peak', action='store_true', help="Simular hora pico")
    args = parser.parse_args()

    data_dir = args.data_dir
    stations = load_stations(os.path.join(data_dir, 'stations.json'))
    edges = load_edges(os.path.join(data_dir, 'edges.json'))
    rules = load_rules(os.path.join(data_dir, 'rules.json'))

    res = find_best_route(args.start, args.goal, edges, rules, peak=args.peak)
    if res:
        print("Costo estimado:", round(res['cost'], 2))
        print("Recorrido:", " -> ".join([stations.get(s, {'name':s})['name'] if isinstance(stations.get(s), dict) else s for s in res['path']]))
    else:
        print("No se encontró ruta con las restricciones dadas.")

if __name__ == '__main__':
    cli()