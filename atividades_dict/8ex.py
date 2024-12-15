# Dicionário para armazenar os produtos
produtos = {
    1: {'nome': 'Monitor LED', 'preco': 800.00, 'quantidade': 2},
    2: {'nome': 'Placa Mãe socket AMD', 'preco': 600.00, 'quantidade': 4},
    3: {'nome': 'Memória RAM 8GB DDR4', 'preco': 200.00, 'quantidade': 20},
    4: {'nome': 'Placa de Vídeo 4GB DDR5', 'preco': 1500.00, 'quantidade': 12},
    5: {'nome': 'SSD 1GB', 'preco': 400.00, 'quantidade': 6},
    6: {'nome': 'Fonte de alimentação 600W', 'preco': 500.00, 'quantidade': 17},
    7: {'nome': 'Processador AMD Ryzen 7', 'preco': 1200.00, 'quantidade': 10}
}

# Função para imprimir o cadastro de produtos
def imprime_produtos(produtos):
    for codigo, detalhes in produtos.items():
        print(f"Código: {codigo}")
        for chave, valor in detalhes.items():
            print(f"{chave.capitalize()}: {valor}")
        print()

# Exibindo o cadastro de produtos
imprime_produtos(produtos)
