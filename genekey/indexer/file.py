import pathlib
import typing  # noqa: F401 @UnusedImport

from genekey.indexer import base


class FileIndexer(base.BaseIndexer):

    def __init__(self, filename: pathlib.Path) -> None:
        super().__init__()
        self._file: typing.TextIO = open(filename)

    def read(self) -> None:
        for line in self._file:
            self.feed(line)
