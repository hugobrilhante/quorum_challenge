import csv


class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        data = []
        with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
