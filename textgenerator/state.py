from collections import defaultdict
from random import choices


class State:
    """
    A class representing a state in a Markov chain. A state represent a word and allow to get randomly the next
    word.

    ...

    Methods
    -------
    __str__ -> None
        returns the word represented by the state

    add_linked_state(word: str) -> None
        registers that a word, passed as argument, follows in the a text the word represented by the state.

    get_transition_value -> str
        returns a word, a string, among those which follows in the a text the word represented by the state.
    """

    def __init__(self, value: str):
        """
        :param value: The word represented by the State object.

        """
        self._value = value
        self._linked_states = defaultdict(int)

    def __str__(self) -> str:
        """
        :return: the word represented by the state

        """
        return self._value

    def add_linked_state(self, word: str) -> None:
        """ Registers that a word, passed as argument, follows in the a text the word represented by the state.

        The method update the object private attribute _linked_states, which is a dictionary with words already added as
        keys, and number of times each of them have been added as values.
        If the argument is a new word, the method sets a new key with value 0; otherwise added 1 to the value for the
        key.

        :param word: The word to be added
        :return: None
        """

        self._linked_states[word] += 1

    def get_transition_value(self) -> str:
        """ Returns a word, a string, among those which follows in the a text the word represented by the state.

        The method picks randomly a word from the keys of the object private attribute _linked_states. The probability
        of each word being chosen is weighted according to the values of  _linked_states.

        :return: the next word
        """

        keys = list(self._linked_states.keys())
        values = list(self._linked_states.values())
        return choices(keys, values)[0]
