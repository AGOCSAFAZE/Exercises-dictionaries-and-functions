# Dicionário com os dados dos clientes
clientes = {
    'Empresa A': 15000.00,
    'Empresa B': 25000.00,
    'Empresa C': 10000.00,
    'Empresa D': 30000.00,
    'Empresa E': 20000.00
}

# Ordenando os clientes pelo valor total de compras (do maior para o menor)
clientes_ordenados = dict(sorted(clientes.items(), key=lambda item: item[1], reverse=True))

# Imprimindo o relatório
print("Relatório de Clientes Potenciais:")
for cliente, total_compras in clientes_ordenados.items():
    print(f"{cliente}: R$ {total_compras:.2f}")
