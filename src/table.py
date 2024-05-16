from column import Column


class Table:
    def __init__(self, cols=[]):
        self.cols = cols

        if len(cols) > 0:
            num_rows = self.cols[0].num_rows()

        for i in range(1, len(cols)):
            if self.cols[i].num_rows() != num_rows:
                raise ValueError("Table must have columns of equal lengths")

    def __eq__(self, other):
        if len(self.cols) != len(other.cols):
            return False

        for i in range(len(self.cols)):
            if self.cols[i] != other.cols[i]:
                return False

        return True
