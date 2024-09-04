import json

def calcula_faturamento() -> None:
    # Abre o arquivo JSON para leitura
    with open('dados.json', 'r') as file:
        # Carrega o conteúdo do arquivo como uma lista de dicionários
        dados = json.load(file)

    # Inicializa listas para armazenar os dias e os valores de faturamento
    lista_dias = []
    lista_faturamento = []
    
    # Itera sobre os dados de faturamento
    for faturamento in dados:
        dia = faturamento['dia']  # Captura o dia do faturamento
        valor = faturamento['valor']  # Captura o valor do faturamento
        
        # Adiciona valores não nulos à lista de faturamento e seus respectivos dias à lista de dias
        if valor != 0:
            lista_faturamento.append(valor)
            lista_dias.append(dia)

    # Determina o menor valor de faturamento e o dia correspondente
    menor_faturamento = min(lista_faturamento)
    dia_menor_faturamento = lista_dias[lista_faturamento.index(menor_faturamento)]

    # Determina o maior valor de faturamento e o dia correspondente
    maior_faturamento = max(lista_faturamento)
    dia_maior_faturamento = lista_dias[lista_faturamento.index(maior_faturamento)]

    # Calcula a média mensal do faturamento
    media_mensal = sum(lista_faturamento) / len(lista_faturamento)

    # Conta o número de dias em que o faturamento diário foi superior à média mensal
    numero_dias = 0
    for faturamento in lista_faturamento:
        if faturamento > media_mensal:
            numero_dias += 1

    # Exibe os resultados calculados
    print(f"Menor faturamento: R${menor_faturamento:.2f}. Ocorrido no dia: {dia_menor_faturamento}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}. Ocorrido no dia: {dia_maior_faturamento}")
    print(f"Valor da média mensal: R${media_mensal:.2f}")
    print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {numero_dias}")

    return

if __name__ == "__main__":
    calcula_faturamento()
