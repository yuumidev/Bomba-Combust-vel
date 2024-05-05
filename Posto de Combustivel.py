class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litrosCarro = valor / self.valorLitro
        if litrosCarro <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litrosCarro
            return f'Foi abastecido {litrosCarro: .2f} litros de {self.tipoCombustivel}'
        else:
            return 'Quantidade de combustível insuficiente'

    def abastecerPorLitro(self, litros):
        valorGasolina = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return f'Valor da conta: {valorGasolina: .2f} reais'
        else:
            return 'Quantidade de combustível insuficiente'

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel


    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade



primeiraBomba = bombaCombustivel('Diesel', 6.39, 50)

print(f'''
    Combustível da primeira bomba:
    {primeiraBomba.tipoCombustivel}
    Valor da primeira bomba:
    {primeiraBomba.valorLitro}
    Quantidade da primeira bomba:
    {primeiraBomba.quantidadeCombustivel}

''')

print('-------------------------------------------------')

print('Abastecendo por valor:')
litrosCarro = primeiraBomba.abastecerPorValor(30)
print(litrosCarro)
print(f'\nNa primeira bomba resta: {primeiraBomba.quantidadeCombustivel: .2f} litros de combustível')

print('-------------------------------------------------')

print('\nAbastecendo por litro:')
valorGasolina = primeiraBomba.abastecerPorLitro(20)
print(valorGasolina)

print(f'\nNa primeira bomba resta: {primeiraBomba.quantidadeCombustivel: .2f} litros de combustível')

print('-------------------------------------------------')
print('Alterando a bomba:')
print('\nAlterando o valor do litro:')
primeiraBomba.alterarValor(5.99)
print(primeiraBomba.valorLitro)

print('\nAlterando tipo de combustível:')
primeiraBomba.alterarCombustivel('Gasolina')
print(primeiraBomba.tipoCombustivel)

print('\nAlterando quantidade de combustível:')
primeiraBomba.alterarQuantidadeCombustivel(100)
print(primeiraBomba.quantidadeCombustivel)

print('-------------------------------------------------')
print('\n\nNovos valores alterados:')
print(f'''
    Combustível da primeira bomba alterado:
    {primeiraBomba.tipoCombustivel}
    Valor da primeira bomba alterado:
    {primeiraBomba.valorLitro}
    Quantidade da primeira bomba alterado:
    {primeiraBomba.quantidadeCombustivel}

''')

print('-------------------------------------------------')

print('Abastecendo por valor:')
litrosCarro = primeiraBomba.abastecerPorValor(30)
print(litrosCarro)
print(f'\nNa primeira bomba resta: {primeiraBomba.quantidadeCombustivel: .2f} litros de combustível')

print('-------------------------------------------------')

print('\nAbastecendo por litro:')
valorGasolina = primeiraBomba.abastecerPorLitro(20)
print(valorGasolina)
print(f'\nNa primeira bomba resta: {primeiraBomba.quantidadeCombustivel: .2f} litros de combustível')