class Pessoa:
    def __init__(self, *filhos, nome = None, idade=58):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    flavio = Pessoa(nome='Flavio')
    feliciano = Pessoa(flavio, nome='Feliciano')
    print(Pessoa.cumprimentar(feliciano))
    print(id(feliciano))
    print(feliciano.cumprimentar())
    print(feliciano.nome)
    print(feliciano.idade)
    for filho in feliciano.filhos:
        print(filho.nome)



