
import argparse
from excellib.grouper import StringGrouper
from excellib.parser import TableParser
from excellib.view import CsvTableView

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('inputfile', action="store", help='planet operate .csv file')
    parser.add_argument('outputfile', action="store", help='filename of new file to create')
    args = parser.parse_args()

    bad_columns = [
        'Revert Build Versions', 'Revert Sw Release', 'Current SW Build Versions',
        'Current Sw Release', 'Upgrade SW Build Versions', 'Upgrade Sw Release',
    ]

    data = ''
    with open(args.inputfile) as f:
        data = f.read()

    groups = StringGrouper(data)
    groups = [g for g in groups if g[0].startswith('Hardware Module Inventory')]

    contents = []
    for group in groups:
        data = TableParser().parse(group)
        view = CsvTableView(data)
        view.remove_columns(*bad_columns)

        def formatter(x):
            # remove last "-01" from end of MFG part numbers
            return x[:-3] if len(x) == 14 else x

        view.format_columns(formatter, 'MFG part number')

        if not contents:
            contents.append(view.render())
        else:
            contents.append(view.render(no_headers=True))

    with open(args.outputfile, 'w') as f:
        for content in contents:
            f.write(content + '\n')
