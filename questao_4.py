def calcula_percentual() -> None:
    # Dicionário contendo o faturamento por estado
    faturamento_estados = {
        "SP": 67836.43,  # Faturamento de São Paulo
        "RJ": 36678.66,  # Faturamento do Rio de Janeiro
        "MG": 29229.88,  # Faturamento de Minas Gerais
        "ES": 27165.48,  # Faturamento do Espírito Santo
        "Outros": 19849.53  # Faturamento de outros estados
    }

    # Inicializa a variável para calcular o faturamento total
    faturamento_total = 0
    # Soma o faturamento de todos os estados para obter o total
    for faturamento in faturamento_estados.values():
        faturamento_total += faturamento

    # Itera sobre cada estado e seu respectivo faturamento
    for estado, faturamento in faturamento_estados.items():
        # Calcula o percentual de cada estado em relação ao faturamento total
        percentual = (faturamento / faturamento_total) * 100
        # Imprime o estado e seu percentual formatado com duas casas decimais
        print(f"{estado}: {percentual:.2f}%")

    return

if __name__ == "__main__":
    calcula_percentual()
