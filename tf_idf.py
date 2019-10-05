from files_collector import FileCollector
from concurrent.futures import ProcessPoolExecutor
from collections import Counter
from tf_idf_logger import LOG


class TFIDF:

    def __init__(self, paths: list):

        """init the tf idf object and """
        self.global_counter = None
        self.logger = LOG
        self.collector = FileCollector(paths, logger=self.logger)
        self.collector.populate_mapper()

    def parse_files(self):
        with ProcessPoolExecutor() as executor:
            for file_word_count in self.collector.mapper:
                self.collector.mapper[file_word_count] = executor.submit(file_word_count.analyze_file)
        for word_counter, process in self.collector.mapper.items():
            self.collector.mapper[word_counter] = process.result()

    def join_counters(self, new_counters=None):
        """
        calc the total freq of all words
        :param new_counters: if new files added calc only the diff
        """
        if not new_counters:
            self.global_counter = Counter()
            for file_word_count in self.collector.mapper.values():
                self.global_counter += file_word_count
        else:
            for counter in new_counters:
                self.global_counter += counter

    def get_n_max_common(self, max_words: int):
        """
        :param max_words: number of common words to print and return
        :return: list of tuples (str: counter)
        """
        error = ""
        if max_words <= 0:
            error = "Max num has to be positive"
        if max_words > len(self.global_counter):
            error = f"Max num has to be smaller or equal to number of words in corpus - {len(self.global_counter)} "
        if error:
            raise ValueError(error)
        print(f"Maximum {max_words} words:")
        most_common = self.global_counter.most_common(max_words)
        for common in most_common:
            print(f"Word ‘{common[0]}’ occurred {common[1]} times")
        self.logger.info(f"Get N Max Common returned:\n {most_common} ")
        return most_common
