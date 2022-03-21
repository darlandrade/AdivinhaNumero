from random import choice
from tkinter import *
from tkinter import messagebox

from contantes import LABEL, LABELFRAME, X, Y, BOTOES_NUMEROS, LABEL_NUMERO, BOTOES


class AdivinhaNumero(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Largura da tela

        # Título
        self.title("Adivinhe o número")
        # Desenho da tela
        self.geometry(f"{X}x{Y}+"
                      f"{int(self.winfo_screenwidth() / 2 - X / 2)}+"
                      f"{int(self.winfo_screenheight() / 2 - Y / 2)}")

        # Criação dos itens na janela
        # Mensagem topo
        l_mensagem_topo = Label(self, text="Este é um jogo de adivinhação. "
                                           "\nEscolha um número e clique em verificar "
                                           "\npara ver se seu palpite está correto", **LABEL)
        l_mensagem_topo.pack(pady=10)

        # Mensagem intervalo número
        self.intervalo = (choice(range(1, 50)), choice(range(50, 100)))
        self.menor_numero = min(self.intervalo)
        self.maior_numero = max(self.intervalo)

        # Divide topo da mensagem do intervalo de números
        divisor = LabelFrame(self, **LABELFRAME)
        divisor.pack()

        self.texto_intervalo = f"Estou pensando em um número entre {self.menor_numero} e {self.maior_numero}"
        self.l_mensagem_intervalo = Label(self, text=self.texto_intervalo, **LABEL)
        self.l_mensagem_intervalo.pack()

        divisor = LabelFrame(self, **LABELFRAME)
        divisor.pack()

        # Botões 0 - 9
        f_botoes_numeros = Frame(self, )
        f_botoes_numeros.pack()
        # Lista para armazenar os botões
        self.botoes = []
        # Cria os botões e adiciona na lista
        for x, botao in enumerate(range(10)):
            self.botoes.append(Button(f_botoes_numeros, text=x, **BOTOES_NUMEROS,
                                      command=lambda num=botao: self.recebe_numeros_escolhidos(num)))
        # Faz o posicionamento dos botões na tela
        for posicao, botao in enumerate(self.botoes):
            if posicao < 5:
                self.botoes[posicao].grid(row=0, column=posicao, pady=10, padx=5, )
            else:
                self.botoes[posicao].grid(row=1, column=posicao - 5)

        # Painel para mostrar o número escolhido
        self.numero_escolhido = ""
        self.l_numero_escolhido = Label(self, text='', **LABEL_NUMERO)
        self.l_numero_escolhido.pack(pady=10)

        # Botão verifica resposta
        self.b_verifica_resposta = Button(self, text="Verificar resposta", **BOTOES,
                                          command=lambda: self.verifica_resposta(
                                              int(self.resposta), self.numero_escolhido))
        self.b_verifica_resposta.pack()

        # Tentativas e acertos
        f_tentativas = Frame(self, )
        f_tentativas.pack()
        self.tentativas = 0
        self.acertos = 0
        self.l_text_tentativas = Label(f_tentativas, text="Tentativas: 0", **LABEL, )
        self.l_text_acertos = Label(f_tentativas, text="Acertos: 0", **LABEL, )
        self.l_text_tentativas.grid(row=0, column=0, pady=10)
        self.l_text_acertos.grid(row=0, column=2)

        # Mensagem numero incorreto
        self.l_numero_incorreto = Label(self, **LABEL)
        self.l_numero_incorreto.pack(pady=5)
        # Resposta
        self.resposta = self.resposta()

    # Recebe o número escolhido ao clicar no botão
    def recebe_numeros_escolhidos(self, n):
        for i, numero in enumerate(self.botoes):
            botao = numero.cget("text")

            if botao == n:
                self.numero_escolhido += str(botao)
        self.imprime_numero_escolhido(self.numero_escolhido)

    # Faz a impressão do número escolhido
    def imprime_numero_escolhido(self, numero):
        self.l_numero_incorreto['text'] = ""
        self.l_numero_escolhido["text"] = str(numero)

    # Cria a resposta para validar com número escolhido
    def resposta(self):
        return str(choice(range(self.menor_numero, self.maior_numero)))

    def verifica_resposta(self, valor_resposta, valor_escolhido):
        if valor_escolhido and self.menor_numero < int(valor_escolhido) < self.maior_numero:
            if valor_resposta == int(valor_escolhido):
                if messagebox.askquestion("Correto!", "Você acertou, \ndeseja jogar novamente?") == "yes":
                    self.acertos += 1
                    self.l_text_acertos['text'] = f"Acertos: {self.acertos}"
                    self.jogar_novamente()
                else:
                    self.quit()
            else:
                if messagebox.askquestion("Game Over!", "Você errou, \ndeseja jogar novamente?") == "yes":
                    self.jogar_novamente()
                    self.tentativas += 1
                    self.l_text_tentativas['text'] = f"Tentativas: {self.tentativas}"
                else:
                    self.quit()
        else:
            self.l_numero_incorreto['text'] = "Escolha um número dentro do intervalo que mencionei"
            self.l_numero_escolhido['text'] = ""
            self.numero_escolhido = ""

    def jogar_novamente(self):
        self.intervalo = (choice(range(1, 50)), choice(range(50, 100)))
        self.menor_numero = min(self.intervalo)
        self.maior_numero = max(self.intervalo)
        self.l_mensagem_intervalo["text"] = f"Estou pensando em um número entre " \
                                            f"{self.menor_numero} e {self.maior_numero}"
        self.l_numero_escolhido["text"] = ""
        self.numero_escolhido = ""






if __name__ == '__main__':
    adivinha = AdivinhaNumero()
    adivinha.mainloop()
