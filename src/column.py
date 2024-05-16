from cell import Cell


class Column:
    def __init__(self, title, cells=[]):
        self.title = title
        self.cells = []
        for val in cells:
            new_cell = val
            if not isinstance(val, Cell):
                new_cell = Cell(val)

            self.cells.append(new_cell)

        self.padding = 1

    def get_max_width(self):
        max = len(self.title)
        for cell in self.cells:
            if len(cell) > max:
                max = len(cell)

        return max + 2 * self.padding

    def num_rows(self):
        return len(self.cells)

    def add_cell(self, cell):
        self.cells.append(cell)

    def get_padding_string(self):
        return " " * self.padding

    def add_padding(self, string):
        return self.get_padding_string() + string + self.get_padding_string()

    def get_title_string(self):
        return self.add_padding(self.title).ljust(self.get_max_width())

    def get_cell_string(self, row_num):
        if row_num not in range(len(self.cells)):
            raise ValueError(f"Row num out of bounds for column '{self.title}'")

        cell = self.cells[row_num]

        return self.add_padding(f"{cell}").ljust(self.get_max_width())

    def __repr__(self):
        return f"{self.title} (Pad: {self.padding}): {self.cells}"

    def __eq__(self, other):
        if self.title != other.title:
            return False

        if self.padding != other.padding:
            return False

        if len(self.cells) != len(other.cells):
            return False

        for i in range(len(self.cells)):
            if self.cells[i] != other.cells[i]:
                return False

        return True
