from itertools import combinations

def gerar_combinacoes(lista, tamanho):
    """
    Função para gerar todas as combinações de tamanho 'tamanho' de uma lista de elementos.

    Argumentos:
    lista: A lista de elementos.
    tamanho: O tamanho das combinações desejadas.

    Retorna:
    Uma lista contendo todas as combinações de tamanho 'tamanho' dos elementos da lista.
    """
    return list(combinations(lista, tamanho))

# Exemplo de uso
elementos = [1, 2, 3, 4]
tamanho_combinacao = 2

todas_combinacoes = gerar_combinacoes(elementos, tamanho_combinacao)
print(f"Todas as combinações de {elementos} de tamanho {tamanho_combinacao} são:")
for combinacao in todas_combinacoes:
    print(combinacao)
