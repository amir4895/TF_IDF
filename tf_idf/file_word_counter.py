from collections import Counter
from nltk.corpus import stopwords

class FileWordCounter:
    stop_words = set(stopwords.words('english'))

    def __init__(self, file_path: str, logger):
        self.file_path = file_path
        self.words_counter = Counter()
        self.counter = 0
        self.logger = logger


    def analyze_file(self):
        self.logger.info(f"Starting analyzing file:{self.file_path}")
        try:
            line_c = 1
            with open(self.file_path) as f_h:
                line = f_h.readline()
                while line:
                    line = line.strip().split()
                    filtered_line = [w for w in line if not w in self.stop_words]

                    self.words_counter.update(filtered_line)
                    self.counter += len(filtered_line)
                    line = f_h.readline()
                    line_c += 1
        except UnicodeDecodeError as e:
            self.logger.error(f"!!!!!Error in parsing file:{self.file_path} Line {line_c} file isn't UTF8!", exc_info=1)
            raise e
        self.logger.info(f"Finish analyzing file:{self.file_path}")
        return self.words_counter

