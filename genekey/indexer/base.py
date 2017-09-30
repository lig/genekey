import collections


class BaseIndexer:

    def __init__(self):
        self._index: dict = collections.Counter()
        self._buffer: str = ''

    def feed(self, text: str) -> None:
        buffer: str = self._buffer

        for char in text:
            pair: str = buffer + char
            if len(pair) == 2:
                self._index[pair] += 1
            buffer = char

        self._buffer = buffer

    def get_index(self) -> dict:
        return dict(self._index)
