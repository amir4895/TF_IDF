import argparse
from files_collector import FileCollector
from concurrent.futures import ProcessPoolExecutor
from collections import Counter
from validation_args_functions import check_not_neg, validate_paths_arg


def main():

    parser = argparse.ArgumentParser(description='TF_IDF arg parser.', add_help=False)
    parser.add_argument('--max­words', dest="max_words", type=check_not_neg, action="store",
                        help='N words with maximal of occurrences', required=True)

    parser.add_argument(dest="paths", nargs='+',  type=validate_paths_arg,
                        help='Paths to text files/folders')

    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')

    args = parser.parse_args()

    file_collector = FileCollector(args.paths)

    with ProcessPoolExecutor() as executor:
        for file_word_count in file_collector.mapper.values():
            executor.submit(file_word_count.analyze_file)

    c = Counter()
    for file_word_count in file_collector.mapper.values():
        c += file_word_count.words_counter

    print(f"Maximum {args.max_words} words:")
    most_common = c.most_common(args.max_words)
    for common in most_common:
        print(f"Word ‘{common[0]}’ occurred {common[1]} times")


if __name__ == "__main__":
    main()
