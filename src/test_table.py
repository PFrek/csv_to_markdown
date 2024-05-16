import unittest
from table import Table
from column import Column


class TestTable(unittest.TestCase):
    def test_creation(self):
        valid_cols = [
            Column("first", [1, 2, 3, 4, 5]),
            Column("second", [6, 7, 8, 9, 10]),
        ]

        table = Table(valid_cols)

        self.assertEqual(
            table,
            Table(
                [
                    Column("first", [1, 2, 3, 4, 5]),
                    Column("second", [6, 7, 8, 9, 10]),
                ]
            ),
        )
