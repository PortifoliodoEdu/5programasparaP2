def soma_naturais(n):
    return n * (n + 1) // 2

def verificar_soma_naturais():
    # Verificando para os primeiros 10 números naturais
    for i in range(1, 11):
        resultado_formula = soma_naturais(i)
        resultado_soma = sum(range(1, i+1))

        print(f'Para n = {i}:')
        print(f'Soma pela fórmula: {resultado_formula}')
        print(f'Soma calculada: {resultado_soma}')

        if resultado_formula == resultado_soma:
            print('As somas são iguais.\n')
        else:
            print('As somas são diferentes.\n')

# Chamando a função para verificar os resultados
verificar_soma_naturais()
