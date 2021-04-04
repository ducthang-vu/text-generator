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

    def __init__(self, words: list[str]):
        """
        :param words: a list of strings representing a text from which generate the Markov chain
        """

        self._states = {}
        for index, word in enumerate(words):
            if index != 0:
                prev = words[index - 1]
                self._states[prev].add_linked_state(word)
                if word not in self._states:
                    self._states[word] = State(word)
            else:
                self._states[word] = State(word)

    def _pick_random_state(self) -> State:
        """
        :return: return randomly one among the states of the chain represented by the object.
        """

        return choice(list(self._states.values()))

    def get_sequence(self, n=100) -> [State]:
        """ returns a list of State objects from the chain represented by the object

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
