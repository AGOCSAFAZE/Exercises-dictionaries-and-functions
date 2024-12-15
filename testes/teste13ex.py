# Dicionário inicial de voos
voos = {
    101: {'origem': 'São Paulo', 'destino': 'Gramado', 'preco': 450.0},
    102: {'origem': 'Rio de Janeiro', 'destino': 'Belo Horizonte', 'preco': 300.0},
    103: {'origem': 'Brasília', 'destino': 'Gramado', 'preco': 500.0},
    104: {'origem': 'Porto Alegre', 'destino': 'São Paulo', 'preco': 350.0}
}

# Exibindo a listagem inicial de voos
print("Lista de voos cadastrados:")
for codigo, detalhes in voos.items():
    print(f"Código: {codigo}, Origem: {detalhes['origem']}, Destino: {detalhes['destino']}")

# Solicitando ao usuário o código do voo que deseja alterar
codigo_voo = int(input("\nDigite o código do voo que deseja modificar: "))

# Verificando se o código existe no dicionário
if codigo_voo in voos:
    # Exibindo detalhes do voo selecionado
    print(f"Voo selecionado - Código: {codigo_voo}, Origem: {voos[codigo_voo]['origem']}, Destino: {voos[codigo_voo]['destino']}")

    # Perguntando se o usuário deseja alterar a origem
    alterar_origem = input("Deseja alterar a origem? (s/n): ").lower()
    if alterar_origem == 's':
        nova_origem = input("Digite a nova origem: ")
        voos[codigo_voo]['origem'] = nova_origem

    # Perguntando se o usuário deseja alterar o destino
    alterar_destino = input("Deseja alterar o destino? (s/n): ").lower()
    if alterar_destino == 's':
        novo_destino = input("Digite o novo destino: ")
        voos[codigo_voo]['destino'] = novo_destino
else:
    print("Código de voo não encontrado!")

# Exibindo a nova listagem de voos
print("\nNova lista de voos cadastrados:")
for codigo, detalhes in voos.items():
    print(f"Código: {codigo}, Origem: {detalhes['origem']}, Destino: {detalhes['destino']}")
