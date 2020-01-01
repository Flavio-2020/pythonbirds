class Pessoa:
    olhos = 2

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
    feliciano.sobrenome = 'Cabral'
    del feliciano.filhos
    feliciano.olhos = 1
    del feliciano.olhos
    print(feliciano.__dict__)
    print(flavio.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(feliciano.olhos)
    print(flavio.olhos)
    print(id(Pessoa.olhos), id(feliciano.olhos), id(flavio.olhos))



