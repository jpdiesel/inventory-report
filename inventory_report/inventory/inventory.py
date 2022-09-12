from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path, encoding="utf8") as file:
            if path.endswith(".csv"):
                dict_list = list(csv.DictReader(file))
            if path.endswith(".json"):
                dict_list = json.load(file)
            if path.endswith(".xml"):
                dict_list = xmltodict.parse(file.read())["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)
