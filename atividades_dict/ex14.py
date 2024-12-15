series = {
    "Breaking Bad": ["Bryan Cranston", "Aaron Paul", "Anna Gunn"],
    "Stranger Things": ["Millie Bobby Brown", "Finn Wolfhard", "David Harbour"],
    "Game of Thrones": ["Emilia Clarke", "Kit Harington", "Peter Dinklage"],
    "Friends": ["Jennifer Aniston", "Courteney Cox", "Matthew Perry"]
}
nome_ator = input('coloque o nome da serie:')

if nome_ator in series:

    print(f"estes são os atores principais'{nome_ator}'")
    for atores in series[nome_ator]:
        print(f"esses sãos os atores'{atores}")        
    else: nome_ator not in series
print('não tem nenhuma serie com esse nome')
#15/16 qstão