from column import Column


class Table:
    def __init__(self, cols=[]):
        self.cols = cols

        if len(self.cols) > 0:
            num_rows = self.cols[0].num_rows()

        for i in range(1, len(cols)):
            if self.cols[i].num_rows() != num_rows:
                raise ValueError("Table must have columns of equal lengths")

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

    def __eq__(self, other):
        if len(self.cols) != len(other.cols):
            return False

        for i in range(len(self.cols)):
            if self.cols[i] != other.cols[i]:
                return False

        return True
