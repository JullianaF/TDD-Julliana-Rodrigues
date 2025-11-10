from item import Item

class ControladorDeItens:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, titulo, detalhes):
        # ainda não implementado
        pass

    def listar_itens(self):
        return [i.como_dict() for i in self.itens]