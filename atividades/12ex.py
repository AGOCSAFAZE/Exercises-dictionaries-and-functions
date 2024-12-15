viagens = {

    1234 : {'origem': 'porto alegre', 'destino': 'pernambuco'},
    4321 : {'origem': 'belohorizonte', 'destino': 'suiça'},
    5432 : {'origem': 'belohorizonte', 'destino': 'Gramado'}

}

#if viagens.items['origem'] == "belohorizonte":
viagens_bh = {codigo: detalhes for codigo, detalhes in viagens.items() if detalhes['origem'] == 'belohorizonte'}

print(viagens_bh)