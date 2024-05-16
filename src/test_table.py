import unittest
from table import Table
from column import Column


class TestTable(unittest.TestCase):
    def test_creation_ok(self):
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

    def test_creation_nok(self):
        invalid_cols = [
            Column("first", [1, 2, 3, 4, 5]),
            Column("second", [6, 8, 9, 10]),
        ]

        with self.assertRaises(ValueError):
            Table(invalid_cols)

    def test_num_rows(self):
        table = Table(
            [
                Column("first", [1, 2, 3, 4, 5]),
                Column("second", [6, 7, 8, 9, 10]),
            ]
        )

        num_rows = table.get_num_rows()

        self.assertEqual(num_rows, 5)

    def test_to_markdown(self):
        table = Table(
            [
                Column("id", [1, 2, 3, 4, 5]),
                Column("name", ["Joe", "Larry", "Sarah", "Doug", "Nostradamus"]),
                Column("age", [25, 98, 31, 19, 230]),
            ]
        )

        markdown = table.to_markdown()

        self.assertEqual(
            markdown,
            """| id | name        | age |
|----|-------------|-----|
| 1  | Joe         | 25  |
| 2  | Larry       | 98  |
| 3  | Sarah       | 31  |
| 4  | Doug        | 19  |
| 5  | Nostradamus | 230 |
""",
        )
