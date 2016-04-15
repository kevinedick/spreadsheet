
from itertools import groupby


class Grouper(object):

    def __init__(self, data, delims='\r'):
        self.data = data
        self.delims = [delims] if type(delims) == str else delims

    def _is_delim(self, content):
        result = max([content == delim for delim in self.delims])
        return result

    def __iter__(self):
        for is_delim, group in groupby(self.data, self._is_delim):
            result = [g for g in group]
            if not is_delim:
                yield result


class StringGrouper(Grouper):

    def __init__(self, data, delims='\r', line_delim='\n'):
        data = data.split(line_delim)
        super(StringGrouper, self).__init__(data, delims=delims)
