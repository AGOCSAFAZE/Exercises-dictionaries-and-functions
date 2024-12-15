
imagens = {

    1234 : {'4k': 'porto alegre',},
    4321 : {'4k': 'belohorizonte',},
    5432 : {'4k': 'belohorizonte',}

}
codigo = []
detalhes = []
for codigo, detalhes in imagens.items():
    if detalhes["4k"] == "belohorizonte":
        print(detalhes)

#imagens_bh = {codigo: detalhes for codigo, detalhes in imagens.items() if detalhes['4k'] == 'belohorizonte' }  //esse é o jeito mais rapido e "facíl"