from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list):
        now = date.today().strftime("%Y-%m-%d")
        fabrication = min([product["data_de_fabricacao"] for product in list])
        expiration = min(
            [
                product["data_de_validade"]
                for product in list
                if product["data_de_validade"] >= now
            ]
        )
        company = [product["nome_da_empresa"] for product in list]
        most_products = max(company, key=company.count)

        return (
            f"Data de fabricação mais antiga: {fabrication}\n"
            f"Data de validade mais próxima: {expiration}\n"
            f"Empresa com mais produtos: {most_products}"
        )
