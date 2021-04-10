"""text-generator main script

This script is a cli interface for running the application.

This file can also be imported as a module and contains the following
functions:
    * generate_text - print a randomly generated text
    * main - the main function of the script
"""

import argparse
from textgenerator.text_generator import TextGenerator


def generate_text(author: str, length: int, words_per_state: int) -> None:
    """ print a randomly generated text

    :param author: the author from which retrieve the corpus
    :param length: the total number of words for the generated text
    :param words_per_state: number of words for each state of Markov chain
    :return: None
    """
    text_gen = TextGenerator(author, words_per_state)
    print(text_gen.get_new_text(length))


def main() -> None:
    """Script main function"""

    parser = argparse.ArgumentParser(description='Text generator.')
    parser.add_argument('-a', '--author', metavar='Author', type=str,
                        help='An author', choices=list(TextGenerator.author_path), required=True)
    parser.add_argument('-l', '--length', metavar='Length', type=int,
                        help='The total number of words', required=True)
    parser.add_argument('-w', '--wordsPerState', metavar='Length', type=int,
                        help='Number of words for every state (default: 1)', default=1)
    args = parser.parse_args()
    generate_text(args.author, args.length, args.wordsPerState)


if __name__ == '__main__':
    main()
