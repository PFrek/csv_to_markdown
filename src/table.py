from column import Column
from cell import Cell


class Table:
    def __init__(self, cols=[], **kwargs):
        self.cols = cols

        if len(self.cols) > 0:
            num_rows = self.cols[0].num_rows()

        for i in range(1, len(cols)):
            if self.cols[i].num_rows() != num_rows:
                raise ValueError("Table must have columns of equal lengths")

        self.none_str = ""
        if "none_str" in kwargs:
            self.none_str = kwargs["none_str"]

    def get_num_rows(self):
        num_rows = 0

        if len(self.cols) > 0:
            num_rows = self.cols[0].num_rows()

        for i in range(1, len(self.cols)):
            if self.cols[i].num_rows() != num_rows:
                raise ValueError(
                    "Table in invalid state: must have columns of equal lengths"
                )

        return num_rows

    def to_markdown(self):
        title_row = "|"
        divider_row = "|"
        for col in self.cols:
            title_row += f"{col.get_title_string()}|"

            divider_row += "-" * col.get_max_width()
            divider_row += "|"

        title_row += "\n"
        divider_row += "\n"

        contents = ""
        for row_num in range(self.get_num_rows()):
            for col in self.cols:
                contents += f"|{col.get_cell_string(row_num)}"

            contents += "|\n"

        return title_row + divider_row + contents

    def __get_titles(self, title_line):
        titles = title_line.split(",")
        if len(titles) == 0:
            raise ValueError("Could not find titles in .csv: empty file")

        return titles

    def from_csv(self, csv):
        lines = list(filter(lambda line: len(line) > 0, csv.split("\n")))
        if len(lines) == 0:
            raise ValueError("Could not read .csv: empty file")

        titles = self.__get_titles(lines[0])

        num_cols = len(titles)
        cols = []

        for i in range(num_cols):
            cols.append(Column(titles[i]))

        for line_num in range(1, len(lines)):
            line = lines[line_num]
            cells = line.split(",")

            if len(cells) != num_cols:
                raise ValueError(f"Mismatched number of columns found in line {
                                 line_num}: {line}")

            for i in range(num_cols):
                val = cells[i]
                if val == "":
                    cols[i].add_cell(Cell(None, self.none_str))
                else:
                    cols[i].add_cell(Cell(cells[i], self.none_str))

        self.cols = cols

    def __eq__(self, other):
        if len(self.cols) != len(other.cols):
            return False

        for i in range(len(self.cols)):
            if self.cols[i] != other.cols[i]:
                return False

        return True
