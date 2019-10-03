import argparse
from files_collector import FileCollector
from concurrent.futures import ProcessPoolExecutor
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description='TF_IDF arg parser.')
    parser.add_argument('-N', '--n_max',  type=int, action="store", help='N words with maximal of occurrences',
                        required=True)
    parser.add_argument('-P', '--paths', nargs='+', help='Paths to text files/folders',
                        required=True)
    args = parser.parse_args()

    file_collector = FileCollector(args.paths)

    with ProcessPoolExecutor() as executor:
        for file_word_count in file_collector.mapper.values():
            executor.submit(file_word_count.analyze_file)

    c = Counter()
    for file_word_count in file_collector.mapper.values():
        c += file_word_count.words_counter
    print(f"The {args.n_max}  most common words are {c.most_common(args.n_max)} ")


if __name__ == "__main__":
    main()
