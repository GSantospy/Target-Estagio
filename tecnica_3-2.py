import xml.etree.ElementTree as ET
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

tree = ET.parse('tecnica_3-2.xml')
root = tree.getroot()

def Faturamento(data):
    faturamentoDiario = [float(dia.find("valor").text) for dia in data if float(dia.find("valor").text) > 0]

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

resultado = Faturamento(root)
print(f"""
Menor valor de faturamento: {locale.currency(resultado['menorFaturamento'], grouping=True)}
Maior valor de faturamento: {locale.currency(resultado['maiorFaturamento'], grouping=True)}
Número de dias com faturamento acima da média: {resultado['acimaDaMedia']}
""")