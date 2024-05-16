import unittest
import os
import argparse

from table import Table
from column import Column


def get_extension(filename):
    return "".join(filename.partition(".")[1:])


def check_files(input, output, force):
    input_ext = get_extension(input)
    if input_ext != ".csv":
        raise ValueError(f"Input file does not have .csv extension: '{input_ext}'")

    if not os.path.isfile(input):
        raise ValueError(f"Input file '{input}' not found")

    output_ext = get_extension(output)
    if output_ext != ".md":
        raise ValueError(f"Output file must have .md extension: '{output_ext}'")

    if os.path.isfile(output):
        if not force:
            raise ValueError(f"Output file '{
                             output}' already exists. To overwrite the file, use the --force flag")


def get_titles(title_line):
    titles = title_line.split(",")
    if len(titles) == 0:
        raise ValueError("Could not find titles in .csv: empty file")

    return titles


def read_csv(csv):
    lines = list(filter(lambda line: len(line) > 0, csv.split("\n")))
    if len(lines) == 0:
        raise ValueError("Could not read .csv: empty file")

    titles = get_titles(lines[0])

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
            cols[i].add_cell(cells[i])

    table = Table(cols)

    return table


def main():
    parser = argparse.ArgumentParser(
        prog="csv_to_md",
        description="Converts .csv files to a markdown table representation",
    )

    parser.add_argument("src_csv", help="The .csv file to be converted")

    parser.add_argument(
        "-o", "--output", help="The name of the .md output file", required=True
    )

    parser.add_argument(
        "-f",
        "--force",
        help="Whether the output file should be overwritten if it already exists",
        action="store_true",
    )

    args = parser.parse_args()

    input = args.src_csv
    output = args.output
    force = args.force

    try:
        check_files(input, output, force)
    except ValueError as e:
        print("Error:", e)
        return

    csv = ""
    with open(input, "r") as f:
        csv = f.read()

    table = None
    try:
        table = read_csv(csv)
    except ValueError as e:
        print("Error:", e)
        return

    if not Table:
        print("Failed to create Table")
        return

    print(table.to_markdown())


main()
