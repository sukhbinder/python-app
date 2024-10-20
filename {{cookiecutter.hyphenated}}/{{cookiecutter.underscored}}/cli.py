import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="{{ cookiecutter.description }}")
    parser.add_argument("name", type=str, help="Dummy argument")
    return parser


def cli():
    "{{ cookiecutter.description }}"
    parser = create_parser()
    args = parser.parse_args()
    mycommand(args)


def mycommand(args):
    print(args)