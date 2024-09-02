import json

with open('tecnica_3.json') as f:
    dadosFaturamento = json.load(f)

def Faturamento(data):
    faturamentoDiario = [dia["faturamento"] for dia in data if dia["faturamento"] > 0]

    if not faturamentoDiario:
        return 'Não hà dias com faturamento.'
    
    menorFaturamento = min(faturamentoDiario)
    maiorFaturamento = max(faturamentoDiario)
    mediaMensal = sum(faturamentoDiario) / len(faturamentoDiario)
    acimaMedia = sum(1 for valor in faturamentoDiario if valor > mediaMensal)

    return {
        "menorFaturamento": menorFaturamento,
        "maiorFaturamento": maiorFaturamento,
        "acimaDaMedia": acimaMedia
    }

resultado = Faturamento(dadosFaturamento)
print(f"""
Menor valor de faturamento: R$ {resultado['menorFaturamento']}
Maior valor de faturamento: R$ {resultado['maiorFaturamento']}
Número de dias com faturamento acima da média: {resultado['acimaDaMedia']}
""")