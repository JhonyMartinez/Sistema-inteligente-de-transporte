# Ruta Inteligente (Simulación para TransMilenio)

## Requisitos
- Python 3.8+

Este sistema calcula la mejor ruta entre estaciones de TransMilenio usando el siguiente modelo:
- **Hechos:** estaciones y enlaces (data/)
- **Reglas:** preferencias (rules.json)
- **Motor:** aplica reglas al costo de cada enlace
- **Búsqueda:** algoritmo Dijkstra adaptado que encuentra la mejor ruta

## Estructura
  ruta-transmilenio/
    data/
      stations.json
      edges.json
      rules.json
    src/
      kb_loader.py
      engine.py
      search.py
      main.py
      tests.py

## Para ejecutarlo
cd ruta-transmilenio/src
python tests.py

python main.py --start PN --goal C85

python main.py --start P80 --goal C85 --peak  (Este de aqui es para simular una hora pico)
