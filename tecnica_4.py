import json

with open('tecnica_4.json') as f:
    faturamentoEstados = json.load(f)

faturamentoTotal = sum(faturamentoEstados.values())
percentuais = {estado: (valor / faturamentoTotal) * 100 for estado, valor in faturamentoEstados.items()}

for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')