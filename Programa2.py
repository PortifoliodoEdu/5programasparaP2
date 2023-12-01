from itertools import permutations

def gerar_permutacoes(lista):
    """
    Função para gerar todas as permutações de uma lista de elementos.

    Argumentos:
    lista: A lista de elementos.

    Retorna:
    Uma lista contendo todas as permutações dos elementos da lista.
    """
    return list(permutations(lista))

# Exemplo de uso
elementos = [1, 2, 3]

todas_permutacoes = gerar_permutacoes(elementos)
print(f"Todas as permutações de {elementos} são:")
for permutacao in todas_permutacoes:
    print(permutacao)
