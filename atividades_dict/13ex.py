
voos = {

    1234 : {'origem': 'porto alegre', 'destino': 'pernambuco'},
    4321 : {'origem': 'belohorizonte', 'destino': 'suiça'},
    5432 : {'origem': 'belohorizonte', 'destino': 'Gramado'}

}
print("Lista de voos cadastrados:")
for codigo, detalhes in voos.items():
    print(f"Código: {codigo}, Origem: {detalhes['origem']}, Destino: {detalhes['destino']}")

#if voos.items['origem'] == "belohorizonte":
#voos_bh = {codigo: detalhes for codigo, detalhes in voos.items() if detalhes['destino'] != 'Gramado'}
    
print(voos)
codigo_voos = str(input('deseja alterar a origem de algum voo? (s/n):'))
codigo_voo = int(input("\nDigite o código do voo que deseja modificar: "))

if codigo_voos in voos.item():
   print(voos)



if codigo_voos == "s":
    print("alterar a origem:")
    nova_origem = input("insira a nova origem:")
    voos[codigo_voos]["origem"] == nova_origem
    print(voos)
if codigo_voos == "n":
    print("obrigado pela atenção")





  
