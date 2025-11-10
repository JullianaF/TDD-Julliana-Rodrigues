from item import Item

class ControladorDeItens:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, titulo, detalhes):
        if any(i.titulo == titulo for i in self.itens):
            raise ValueError("Já existe um item com esse título.")
        novo_item = Item(titulo, detalhes)
        self.itens.append(novo_item)

    def listar_itens(self):
        return [i.como_dict() for i in self.itens]