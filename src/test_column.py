import unittest
from column import Column
from cell import Cell


class TestColumn(unittest.TestCase):
    def test_max_width(self):
        col = Column("test", ["one", Cell("two"), "three", "four", "five"])

        max_width = col.get_max_width()

        self.assertEqual(max_width, 5 + 2 * col.padding)

    def test_empty_width(self):
        col = Column("no")

        max_width = col.get_max_width()

        self.assertEqual(max_width, 2 + 2 * col.padding)

    def test_empty_title_width(self):
        col = Column("")

        max_width = col.get_max_width()

        self.assertEqual(max_width, 0 + 2 * col.padding)

    def test_title_string(self):
        col = Column("hi", [Cell(1), Cell(2), Cell(2000), Cell(None)])

        title_string = col.get_title_string()

        self.assertEqual(title_string, " hi   ")

    def test_title_string_padding(self):
        col = Column("title")
        col.padding = 5

        title_string = col.get_title_string()

        self.assertEqual(title_string, "     title     ")

    def test_cell_string(self):
        col = Column("title", [Cell(1), Cell(2), Cell(3), Cell(None), Cell(4)])

        strings = []
        for i in range(col.num_rows()):
            strings.append(col.get_cell_string(i))

        self.assertEqual(
            strings,
            [
                " 1     ",
                " 2     ",
                " 3     ",
                "       ",
                " 4     ",
            ],
        )
