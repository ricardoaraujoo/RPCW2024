import json

with open('mapa-virtual.json') as f:
    data = json.load(f)

mapa = {}

for cidade in data["cidades"]:
    mapa[cidade['nome']] = cidade['id']

for cidade in data["cidades"]:
    if cidade['distrito'] in mapa:
        cidade['distrito'] = mapa[cidade['distrito']]

with open('mapa-virtual.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)