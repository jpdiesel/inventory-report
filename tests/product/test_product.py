from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        "Espada do Mihawk",
        "OP",
        "2022-09-09",
        "2023-09-09",
        "007",
        "Tire das costas e sole"
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == "Espada do Mihawk"
    assert new_product.nome_da_empresa == "OP"
    assert new_product.data_de_fabricacao == "2022-09-09"
    assert new_product.data_de_validade == "2023-09-09"
    assert new_product.numero_de_serie == "007"
    assert new_product.instrucoes_de_armazenamento == "Tire das costas e sole"
