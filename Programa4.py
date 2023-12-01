def produto_cartesiano(conjunto1, conjunto2):
    """
    Função para calcular o produto cartesiano entre dois conjuntos.

    Argumentos:
    conjunto1: O primeiro conjunto.
    conjunto2: O segundo conjunto.

    Retorna:
    O produto cartesiano entre os dois conjuntos.
    """
    return [(x, y) for x in conjunto1 for y in conjunto2]

# Exemplo de uso
conjunto_a = {1, 2}
conjunto_b = {'a', 'b', 'c'}

resultado_produto_cartesiano = produto_cartesiano(conjunto_a, conjunto_b)
print(f"O produto cartesiano entre {conjunto_a} e {conjunto_b} é:")
print(resultado_produto_cartesiano)
