from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Espada do Mihawk",
        "OP",
        "2022-09-09",
        "2023-09-09",
        "007",
        "Tire das costas e sole"
    )

    assert product.__repr__() == (
        "O produto Espada do Mihawk"
        " fabricado em 2022-09-09"
        " por OP com validade"
        " até 2023-09-09"
        " precisa ser armazenado Tire das costas e sole."
    )
