stringOriginal = input("Digite algo: ")
stringInvertida = ''

for i in range(len(stringOriginal) -1, -1, -1):
    stringInvertida += stringOriginal[i]

print(f"""
String original: {stringOriginal}
String invertida: {stringInvertida}
""")