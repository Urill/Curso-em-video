def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] > 7:
            r['Situação'] = 'Boa'
        elif 5 < r['Média'] < 7:
            r['Situação'] = 'Mediana'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 1.5, sit=False)
print(resp)