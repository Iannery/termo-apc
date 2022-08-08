import random
def retorna_termo():
    lista5 = []
    with open("verbos", encoding = 'utf-8') as f:
        lista = f.read().splitlines()
    for elem in lista:
        if len(elem) == 5:
            lista5.append(elem)
    return random.choice(lista5)