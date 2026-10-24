# Sistema Simples de Gestão Financeira e Cálculo de Médias

def calcular_media_notas(notas):
    """Calcula a média de uma lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

def calcular_desconto(valor, percentual):
    """Aplica um desconto percentual a um valor."""
    return valor - (valor * (percentual / 100))

if __name__ == "__main__":
    print("=== Módulo de Utilitários de Cálculo ===")
    
    # Exemplo 1: Média de Notas
    lista_notas = [8.5, 7.0, 9.2, 8.0]
    media = calcular_media_notas(lista_notas)
    print(f"Notas: {lista_notas}")
    print(f"Média do aluno: {media:.2f}\n")
    
    # Exemplo 2: Cálculo de Desconto
    preco_original = 150.0
    percentual_desc = 10
    preco_final = calcular_desconto(preco_original, percentual_desc)
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Preço com {percentual_desc}% de desconto: R$ {preco_final:.2f}")