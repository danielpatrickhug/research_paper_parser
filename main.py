from argparse import ArgumentParser
from parser import Parser

def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-i', '--input', help='Input file path', required=True)
    #arg_parser.add_argument('-m', '--model_name', help='Model name', required=True)

    args = arg_parser.parse_args()
    parser = Parser(args.input)
    parser.parse()


if __name__ == '__main__':
    main()