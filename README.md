
Projeto Engenharia de Software II

Objetivo do Projeto
Este projeto tem como objetivo estudar e implementar padrões de design, especificamente o padrão Singleton, e entender como ele pode ser aplicado em um jogo de forca. O jogo da forca é um clássico onde o jogador tenta adivinhar uma palavra secreta, letra por letra, com um número limitado de tentativas.

Padrão Singleton
O que é o Padrão Singleton?
O padrão Singleton é um padrão de design estrutural que assegura que uma classe tenha apenas uma única instância durante a execução do programa. Além disso, fornece um ponto de acesso global a essa instância, garantindo que o objeto seja reutilizado sempre que necessário.
Esse padrão é útil quando você precisa de um único objeto para gerenciar recursos compartilhados ou para garantir um ponto único de controle, como em configurações globais, conexões de banco de dados ou até mesmo em jogos, como o caso deste projeto.

Como o Padrão Singleton é aplicado neste projeto?
Neste projeto, o padrão Singleton é aplicado na classe ExibidorDePalavra, que é responsável por gerenciar e exibir a palavra do jogo da forca. O objetivo do Singleton aqui é garantir que apenas uma instância da classe ExibidorDePalavra seja criada, mesmo que o jogo seja executado várias vezes ou que a classe seja acessada por diferentes partes do código.
Ao usar o padrão Singleton, evitamos o desperdício de memória e recursos, além de ter um controle centralizado sobre o estado do jogo, como as letras adivinhadas e a palavra secreta.

Exemplo de Implementação do Padrão Singleton:

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

Vantagens do Padrão Singleton
Controle centralizado: Garante que toda a aplicação use a mesma instância de um objeto, como o ExibidorDePalavra no jogo, tornando o controle do estado do jogo mais simples e seguro.
Uso de recursos otimizado: A criação de uma única instância evita o consumo desnecessário de memória e recursos, que poderia ocorrer se novas instâncias fossem criadas repetidamente.

Desvantagens do Padrão Singleton
Dificuldade de testes: Como a instância é única, pode ser mais difícil realizar testes unitários isolados, já que o comportamento do código pode depender dessa instância global.
Acoplamento forte: O uso de uma instância única em várias partes do sistema pode levar a um acoplamento forte entre essas partes, o que pode tornar a manutenção mais complexa no futuro.

Como Rodar o Projeto
Para rodar o jogo da forca, siga os passos abaixo:

1. Clone o repositório:
   git clone https://github.com/seu-usuario/Engenharia-de-Software-II.git

2. Navegue até a pasta do projeto:
   cd Engenharia-de-Software-II

3. Execute o código para jogar o jogo da forca:
   python jogo_forca.py

Conclusão

O padrão Singleton é uma técnica poderosa e simples de ser implementada, mas deve ser utilizado com cautela. Ele garante a unicidade de instâncias de objetos importantes para o controle centralizado de uma aplicação, mas pode trazer desafios quando se trata de testes e flexibilidade.
Neste projeto, aplicamos o Singleton no jogo da forca para garantir que apenas uma instância do objeto que gerencia a exibição da palavra seja criada, evitando problemas de recursos e tornando o código mais controlado.

