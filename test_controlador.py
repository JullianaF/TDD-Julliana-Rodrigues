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

def test_titulo_vazio_ou_duplicado():
    c = ControladorDeItens()
    c.adicionar_item("Estudar", "Aprender testes")

    with pytest.raises(ValueError):
        c.adicionar_item("", "Sem título")

    with pytest.raises(ValueError):
        c.adicionar_item("Estudar", "Duplicado")

def test_finalizar_e_remover_item():
    c = ControladorDeItens()
    c.adicionar_item("Estudar", "Aprender TDD")

    c.finalizar_item("Estudar")
    assert c.listar_itens()[0]["estado"] == "concluído"

    c.remover_item("Estudar")
    assert len(c.listar_itens()) == 0
