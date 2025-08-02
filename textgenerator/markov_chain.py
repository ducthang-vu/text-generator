from textgenerator.state import State
from random import choice


class MarkovChain:
    """
    A class representing a text as a Markov chain, each chain state being a word of said text.

    ...

    Methods
    -------
    get_sequence(n=100) -> [State]
       get a list of State objects from the chain represented by the object, in such a way that each
       state is a valid and random Markov chain transition of the previous.
    """

    def __init__(self, words: list[str], words_per_state=1):
        """
        :param words: a list of strings representing a text from which generate the Markov chain
        """

        self._words_per_state = words_per_state
        self._states = {}
        self._set_states(words)

    def _set_states(self, words: list[str]) -> None:
        """Set the _states attribute.

        :param words:  a list of strings representing a text from which generate the Markov chain.
        """
        for i in range(len(words) - self._words_per_state + 1):
            new_value = ' '.join(words[i: i + self._words_per_state])
            if new_value not in self._states:
                self._states[new_value] = State(new_value)
            if i:
                prev_value = ' '.join(words[i - 1: i + self._words_per_state - 1])
                self._states[prev_value].add_linked_state(new_value)

    def _pick_random_state(self) -> State:
        """
        :return: return randomly one among the states of the chain represented by the object.
        """

        return choice(list(self._states.values()))

    def get_sequence(self, n=100) -> list[State]:
        """ Returns a list of State objects from the chain represented by the object

        The method picks a random state among the states of the chain and push it into the result list. Then gets the
        next value by calling the get_transition_value method, and adding the corresponding state to the result list.
        The list returned when the total number of state is equal to the number passed as argument.

        :param n: the number of state required, default is 100
        :return: a list of State objects
        """

        sequence = [self._pick_random_state()]
        while len(sequence) < n:
            last: State = sequence[-1]
            try:
                next_word = last.get_transition_value()
                sequence.append(self._states[next_word])
            except IndexError:
                sequence.append(self._pick_random_state())
        return sequence
