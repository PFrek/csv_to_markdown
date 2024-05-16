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


def read_csv(input):
    print(f"Reading csv from '{input}'")
    csv = ""
    with open(input, "r") as f:
        csv = f.read()

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


def write_markdown(output, markdown):
    mode = "w"

    if not os.path.exists(output):
        mode = "x"
        print(f"Creating new output file: {output}")

    print(f"Writing markdown to file: {output}")
    with open(output, mode) as f:
        f.write(markdown)


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

    parser.add_argument(
        "-v",
        "--verbose",
        help="Prints the converted markdown to stdout",
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

    table = None
    try:
        table = read_csv(input)
    except ValueError as e:
        print("Error:", e)
        return

    if not Table:
        print("Failed to create Table")
        return

    markdown = table.to_markdown()

    if args.verbose:
        print("Converted markdown:")
        print(markdown)

    write_markdown(output, markdown)


main()
