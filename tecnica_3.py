import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

with open('tecnica_3.json') as f:
    dadosFaturamento = json.load(f)

def Faturamento(data):
    faturamentoDiario = [dia["valor"] for dia in data if dia["valor"] > 0]

    if not faturamentoDiario:
        return 'Não há dias com faturamento.'
    
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
Menor valor de faturamento: {locale.currency(resultado['menorFaturamento'], grouping=True)}
Maior valor de faturamento: {locale.currency(resultado['maiorFaturamento'], grouping=True)}
Número de dias com faturamento acima da média: {resultado['acimaDaMedia']}
""")