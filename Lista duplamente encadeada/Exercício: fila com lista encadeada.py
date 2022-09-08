class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDupla:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista esta vazia')
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp


class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()

    def fila_vazia(self):
        return self.lista.lista_vazia()

    def enfileirar(self, valor):
        self.lista.insere_final(valor)

    def desinfileirar(self):
        return self.lista.excluir_inicio()

    def ver_inicio(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.mostrar_no()


fila = FilaListaEncadeada()
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(20)
fila.enfileirar(40)
fila.ver_inicio()
fila.desinfileirar()
fila.ver_inicio()
fila.desinfileirar()
fila.ver_inicio()
fila.desinfileirar()
fila.ver_inicio()
fila.desinfileirar()
fila.ver_inicio()
fila.desinfileirar()
fila.ver_inicio()
fila.desinfileirar()
fila.ver_inicio()
