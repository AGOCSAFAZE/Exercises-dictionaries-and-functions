# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Inicializa um dicionário vazio para contar os caracteres
contador_caracteres = {}

# Itera sobre cada caractere na frase//comando que passa por todos os caracteres
for caractere in frase:
    # Converte o caractere para maiúsculo para tratar de forma case-insensitive
    caractere = caractere.upper()
    # Se o caractere já está no dicionário, incrementa o contador
    if caractere in contador_caracteres:
        contador_caracteres[caractere] += 1
    # Caso contrário, adiciona o caractere ao dicionário com contador 1
    else:
        contador_caracteres[caractere] = 1

# Imprime o dicionário resultante
print(contador_caracteres)
