def inverte_string(string_inicial: str) -> str:
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Percorre a string original de trás para frente usando um loop
    # 'range(len(string_inicial) - 1, -1, -1)' começa do último caractere e vai até o primeiro
    for caractere in range(len(string_inicial) - 1, -1, -1):
        # Adiciona cada caractere na nova string invertida
        string_invertida += string_inicial[caractere]

    # Retorna a string que foi construída na ordem inversa
    return string_invertida

if __name__ == "__main__":
    string_inicial = input("Informe uma string\n")
    
    # Chama a função inverte_string para inverter a string fornecida
    string_invertida = inverte_string(string_inicial)
    
    # Imprime a string invertida
    print(string_invertida)
