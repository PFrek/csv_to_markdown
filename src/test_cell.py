import unittest
from cell import Cell


class TestCell(unittest.TestCase):
    def test_repr_string(self):
        cell = Cell("hello")

        r = f"{cell}"

        self.assertEqual(r, "hello")

    def test_repr_num(self):
        cell = Cell(5)

        r = f"{cell}"

        self.assertEqual(r, "5")

    def test_repr_none(self):
        cell = Cell(None)

        r = f"{cell}"

        self.assertEqual(r, "")

    def test_len_string(self):
        cell = Cell("Triad")

        length = len(cell)

        self.assertEqual(length, 5)

    def test_len_num(self):
        cell = Cell(4.9)

        length = len(cell)

        self.assertEqual(length, 3)

    def test_len_none(self):
        cell = Cell(None)

        length = len(cell)

        self.assertEqual(length, 0)
