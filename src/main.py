import os
import argparse

from table import Table


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


def read_csv(input):
    print(f"Reading csv from '{input}'")
    csv = ""
    with open(input, "r") as f:
        csv = f.read()

    return csv


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

    parser.add_argument(
        "--none_str",
        help="The string used to represent an empty cell",
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
    try:
        csv = read_csv(input)
    except Exception as e:
        print("Error:", e)
        return

    none_str = ""
    if args.none_str:
        none_str = args.none_str
    table = Table([], none_str=none_str)
    try:
        table.from_csv(csv)
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
