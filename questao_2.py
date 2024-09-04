def pertence_fibonacci(n: int) -> bool:
    # Inicia uma lista com os dois primeiros números da sequência de Fibonacci
    sequencia = [0, 1]
    
    # Verifica se o número n é 0 ou 1, que já estão na sequência inicial
    if n not in sequencia:
        # Continua gerando a sequência de Fibonacci até que n seja encontrado ou ultrapassado
        while True:
            # Pega os dois últimos valores da sequência
            ultimo_valor = sequencia[-1]
            penultimo_valor = sequencia[-2]
            # Calcula o próximo número na sequência
            proximo_valor = ultimo_valor + penultimo_valor
            
            # Se n for igual ao próximo valor, ele pertence à sequência
            if n == proximo_valor:
                return True
            # Se n for menor que o próximo valor, ele não pertence à sequência
            elif n < proximo_valor:
                return False
            else:
                # Adiciona o próximo valor à sequência e continua o loop
                sequencia.append(proximo_valor)
                continue

    # Se n for 0 ou 1, retorna True, pois eles pertencem à sequência inicial
    return True

if __name__ == "__main__":
    # Solicita ao usuário um número para verificar se pertence à sequência de Fibonacci
    n = int(input("Informe o número a ser verificado\n"))
    # Chama a função para verificar e armazena o resultado
    pertence = pertence_fibonacci(n)
    # Exibe o resultado para o usuário
    if pertence:
        print("O número pertence à sequência.")
    else:
        print("O número não pertence à sequência.")
