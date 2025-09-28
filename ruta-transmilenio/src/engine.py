from typing import Dict
import math

def apply_rules_to_edge(edge: Dict, rules: Dict, state: Dict) -> float:
    
    base_time = float(edge.get('time', 1.0))
    cost = base_time

    # Penalización por transferencia
    if state.get('transfer', False):
        cost += float(rules.get('transfer_penalty', 0.0))

    # Evitar líneas
    avoid_lines = set(rules.get('avoid_lines', []))
    if edge.get('line') in avoid_lines:
        cost *= float(rules.get('avoid_line_multiplier', 1.0))

    # Preferir líneas
    prefer_lines = set(rules.get('prefer_lines', []))
    if edge.get('line') in prefer_lines:
        cost *= float(rules.get('prefer_line_multiplier', 1.0))

    # Requerir accesibilidad
    if rules.get('require_accessible', False) and not edge.get('accessible', True):
        return math.inf

    # Factor por distancia
    distance_factor = float(rules.get('distance_factor', 0.0))
    if distance_factor:
        cost += distance_factor * float(edge.get('distance', 0.0))

    # Hora pico: multiplicadores por línea
    peak_cfg = rules.get('peak', {})
    if state.get('peak', False) and peak_cfg.get('enabled', False):
        mults = peak_cfg.get('multiplier_by_line', {})
        line_mult = float(mults.get(edge.get('line'), 1.0))
        cost *= line_mult

    return cost