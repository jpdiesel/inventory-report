from xml.etree import ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)
        root = list(tree.getroot())
        dict_list = []
        prod_dict = {}

        for index in range(len(root)):
            for prod in root[index]:
                prod_dict[prod.tag] = prod.text
            dict_list.append(prod_dict)
            prod_dict = {}
        return dict_list
