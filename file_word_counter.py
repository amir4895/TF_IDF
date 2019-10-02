from collections import Counter

class FileWordCounter:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.words_counter = Counter()
        self.counter = 0
        self.analyze_file()

    def analyze_file(self):
        try:
            line_c = 1
            with open(self.file_path) as f_h:
                line = f_h.readline()
                while line:
                    line = line.strip().split()
                    self.words_counter.update(line)
                    self.counter += len(line)
                    line = f_h.readline()
                    line_c+=1
        except UnicodeDecodeError:
            print(f"\n\n\n\n\n\n{self.file_path}! {line_c}!!!!!!")
            raise Exception


