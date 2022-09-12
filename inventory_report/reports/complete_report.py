from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)
        products = dict()
        for product in list:
            company = product["nome_da_empresa"]
            if company in products:
                products[company] += 1
            else:
                products[company] = 1

        products_by_company = [
            f'- {key}: {value}\n'
            for (key, value) in products.items()
        ]

        return (
            f'{simple_report}\n'
            "Produtos estocados por empresa:\n"
            f'{"".join(count for count in products_by_company)}'
        )
