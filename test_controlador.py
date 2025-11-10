import pytest
from controlador import ControladorDeItens

def test_adicionar_item():
    c = ControladorDeItens()
    c.adicionar_item("Ler livro", "Ler sobre TDD em Python")
    itens = c.listar_itens()

    assert len(itens) == 1
    assert itens[0]["titulo"] == "Ler livro"
    assert itens[0]["detalhes"] == "Ler sobre TDD em Python"
    assert itens[0]["estado"] == "pendente"
