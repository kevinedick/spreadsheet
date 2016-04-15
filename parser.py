
import tablib


class Parser(object):

    def clean_csv(self, content):
        line = content.strip()  # remove outer whitespace
        line = line.rstrip(',')  # remove last ","
        line = ','.join([item.strip() for item in line.split(',')])  # remove inner whitespaces
        return line

    def parse(self, data):
        raise Exception


class TableParser(Parser):
    title_location = 0
    header_location = 1
    data_location = 2

    def __init__(self, *args):
        self.rules = args

    def get_title(self, data):
        return data[self.title_location]

    def get_headers(self, data):
        return data[self.header_location].split(',')

    def get_rows(self, data):
        body = data[self.data_location:]
        return [row.split(',') for row in body]

    def parse(self, data):
        data = [self.clean_csv(d) for d in data]
        dataset = tablib.Dataset()
        dataset.headers = self.get_headers(data)
        for row in self.get_rows(data):
            dataset.append(row)
        return dataset
