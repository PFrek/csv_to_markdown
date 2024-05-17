# CSV to Markdown converter

Simple program in Python that converts a .csv file to an equivalent table in .md

## Usage

Run csv_to_md.sh or (src/main.py) passing the required arguments:

usage: csv_to_md.sh [-h] [-o OUTPUT] [-f] [-v] [-t] [--none_str NONE_STR] src_csv

Converts .csv files to a markdown table representation

positional arguments:
  src_csv               The .csv file to be converted

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The name of the .md output file
  -f, --force           Whether the output file should be overwritten if it already exists
  -v, --verbose         Prints the converted markdown to stdout
  -t, --test            Converts the file without writing to the output
  --none_str NONE_STR   The string used to represent an empty cell


## Example:

```
$ cat input.csv

id,name,age
1,Joe,25
2,Larry,98
3,Sarah,31
4,Doug,19

$ ./csv_to_md.sh input.csv -o output.md -v

Reading csv from 'input.csv'
Converted markdown:
| id | name  | age |
|----|-------|-----|
| 1  | Joe   | 25  |
| 2  | Larry | 98  |
| 3  | Sarah | 31  |
| 4  | Doug  | 19  |

Creating new output file: output.md
Writing markdown to file: output.md

$ cat output.md

| id | name  | age |
|----|-------|-----|
| 1  | Joe   | 25  |
| 2  | Larry | 98  |
| 3  | Sarah | 31  |
| 4  | Doug  | 19  |
```
