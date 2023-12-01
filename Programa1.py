def calcular_fecho_transitivo(grafo):
    """
    Função para calcular o fecho transitivo de um grafo representado por uma matriz de adjacência.

    Argumentos:
    grafo: Uma matriz que representa o grafo onde grafo[i][j] = 1 indica a existência de uma aresta de i para j.

    Retorna:
    fecho: O fecho transitivo do grafo, onde fecho[i][j] = 1 indica que há um caminho de i para j no grafo.
    """
    fecho = [linha[:] for linha in grafo]  # Inicializa o fecho com a mesma estrutura do grafo

    # Algoritmo para calcular o fecho transitivo usando o método de Warshall
    for k in range(len(grafo)):
        for i in range(len(grafo)):
            for j in range(len(grafo)):
                fecho[i][j] = fecho[i][j] or (fecho[i][k] and fecho[k][j])

    return fecho

# Exemplo de uso
grafo = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

print("Grafo original:")
for linha in grafo:
    print(linha)

fecho_transitivo = calcular_fecho_transitivo(grafo)

print("\nFecho transitivo:")
for linha in fecho_transitivo:
    print(linha)
