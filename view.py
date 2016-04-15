

class View(object):

    def __init__(self, dataset):
        self.dataset = dataset

    def render(self):
        raise Exception


class CsvTableView(View):

    def remove_columns(self, *args):
        for header in args:
            if header in self.dataset.headers:
                del self.dataset[header]

    def format_columns(self, function, *args):
        for column in args:
            self.dataset.add_formatter(column, function)

    def render(self, no_headers=False):
        result = self.dataset.csv
        if no_headers:
            headers = [h for h in self.dataset.headers]
            self.dataset.headers = []
            result = self.dataset.csv
            self.dataset.headers = headers
        return result
