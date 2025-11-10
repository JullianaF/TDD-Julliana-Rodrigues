class Item:
    def __init__(self, titulo, detalhes):
        if not titulo:
            raise ValueError("O título do item não pode ser vazio.")
        self.titulo = titulo
        self.detalhes = detalhes
        self.estado = "pendente"

    def finalizar(self):
        self.estado = "concluído"

    def como_dict(self):
        return {"titulo": self.titulo, "detalhes": self.detalhes, "estado": self.estado}

