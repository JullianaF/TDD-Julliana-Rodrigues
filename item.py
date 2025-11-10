class Item:
    def __init__(self, titulo, detalhes):
        self.titulo = titulo
        self.detalhes = detalhes
        self.estado = "pendente"

    def como_dict(self):
        # erro proposital: campo errado
        return {"titulo": self.titulo, "descricao": self.detalhes, "estado": self.estado}