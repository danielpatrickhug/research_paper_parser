from argparse import ArgumentParser
from parser import Parser
from utils import download_arxiv_paper, remove_arxiv_paper, zip_output_dir

def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-i', '--id', help='Arxiv paper id', required=True)
    arg_parser.add_argument('-m', '--model-name', help='Model name(publaynet)', required=True)
    args = arg_parser.parse_args()
    file_name = download_arxiv_paper(args.id)
    parser = Parser(file_name, args.id, args.model_name)
    parser.parse()
    remove_arxiv_paper(file_name)
    zip_output_dir(args.id)



if __name__ == '__main__':
    main()