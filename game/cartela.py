import random


class Cartela:
    COLUNAS = [
        range(1, 16),    
        range(16, 31),   
        range(31, 46),   
        range(46, 61),   
        range(61, 76),  
    ]

    def __init__(self, numeros=None):
        self.numeros = (
            numeros if numeros is not None
            else self.gerar_cartela()
        )
        self.marcados = set()

    def gerar_cartela(self):
        colunas = [
            random.sample(list(faixa), 5)
            for faixa in self.COLUNAS
        ]

        cartela = [
            [colunas[coluna][linha] for coluna in range(5)]
            for linha in range(5)
        ]

        cartela[2][2] = 0
        return cartela

    def marcar(self, numero):
        if numero == 0:
            return False

        pertence = any(
            numero in linha for linha in self.numeros
        )

        if not pertence:
            return False

        self.marcados.add(numero)
        return True

    def exibir(self):
        for linha in self.numeros:
            print("  ".join(f"{n:2}" for n in linha))

#testes
C = Cartela() #cria instância
C.exibir() #exibe cartela
