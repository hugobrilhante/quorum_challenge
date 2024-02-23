from abc import ABC
from abc import abstractmethod
import csv


class Parser(ABC):
    @abstractmethod
    def load_data(self):
        pass


class CSVParser(Parser):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = []
        with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
