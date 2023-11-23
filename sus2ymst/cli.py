import argparse

from sus2ymst import ErrorMessage, Sus2Ymst


def main():
    parser = argparse.ArgumentParser(description="Convert sus to ymst")
    parser.add_argument("sus_file", help="sus file path")
    parser.add_argument(
        "-o",
        "--output_file",
        help="output file path",
        default="notation.txt",
        required=False,
    )
    args = parser.parse_args()

    sus2ymst = Sus2Ymst()

    notation_txt = sus2ymst.load(args.sus_file)

    error_messages: list[ErrorMessage] = sus2ymst.get_error_messages()
    if error_messages:
        for error_message in error_messages:
            print(error_message)

    with open(args.output_file, "w") as f:
        f.write(notation_txt)
