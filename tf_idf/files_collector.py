from pathlib import Path
from .file_word_counter import FileWordCounter
from os import path as os_path


class FileCollector:

    def __init__(self, paths: list, logger):
        """
        :param paths: list of paths to txt files and or directories
        """
        self.paths = paths
        self.paths_as_set = set()
        self.mapper = {}
        self.logger = logger

    def populate_mapper(self):
        """
        function traverse all paths and populate the mapper
        """
        for arg_path in self.paths:
            if os_path.exists(arg_path):
                if os_path.isfile(arg_path):
                    self.paths_as_set.add(Path(arg_path))
                if os_path.isdir(arg_path):
                    for file_path in Path(arg_path).glob('**/*.txt'):
                        self.paths_as_set.add(file_path)

        for path in self.paths_as_set:
            self.mapper[FileWordCounter(file_path=path, logger=self.logger)] = True
