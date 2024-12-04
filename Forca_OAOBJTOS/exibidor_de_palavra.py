
class ExibidorDePalavra:
    _instancia = None

    def __new__(cls, palavra):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.palavra = palavra
            cls._instancia.letras_adivinhadas = []
        return cls._instancia

    def adicionar_letra_adivinhada(self, letra):
        if letra not in self.letras_adivinhadas:
            self.letras_adivinhadas.append(letra)

    def exibir(self):
        exibicao = ""
        for letra in self.palavra:
            if letra in self.letras_adivinhadas:
                exibicao += letra
            else:
                exibicao += "_"
        return exibicao
