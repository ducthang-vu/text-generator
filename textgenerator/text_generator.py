from textgenerator.markov_chain import MarkovChain
from pathlib import Path
from re import sub

from textgenerator.state import State


class TextGenerator:
    """
    A class representing a text generator.

    ...
    Attributes
    author_path: dict
        a dictionary with authors name as keys, and the path for retrieving the corresponding corpus.

    ...

    Methods
    -------
    get_new_text(text_len=100 -> str
       gets a randomly generated text, with the number of words passed as argument.
    """

    author_path = {
        'katy_perry': 'corpus/katy_perry',
        'lady_gaga': 'corpus/lady_gaga',
        'saint_paul': 'corpus/saint_paul'
    }

    def __init__(self, author: str, words_per_state=1):
        """
        :param author: The author name, must be a key of author_path class attribute
        """

        corpus = Path(TextGenerator.author_path[author]).glob('**/*')
        text = ''
        for file in corpus:
            with open(file) as f:
                text += ' ' + sub(r'[^a-zA-Z \'\n-]', '', f.read()).lower()
        self._chain = MarkovChain(text.split(), words_per_state)

    def get_new_text(self, text_len=100) -> str:
        """ gets a randomly generated text, with the number of words passed as argument.

        :param text_len: The total number of word for the returned text; default is 100.
        :return: the randomly generated text
        """

        sequence: list[State] = self._chain.get_sequence(text_len)
        generated: list[str] = [str(sequence[0])] + [str(state).split()[-1] for state in sequence[1:]]
        return ' '.join(generated)
