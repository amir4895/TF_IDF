import argparse
from validation_args_functions import check_not_neg, validate_paths_arg
from tf_idf import TFIDF


def main():

    parser = argparse.ArgumentParser(description='TF_IDF arg parser.', add_help=False)
    parser.add_argument('--max­words', dest="max_words", type=check_not_neg, action="store",
                        help='N words with maximal of occurrences', required=True)

    parser.add_argument(dest="paths", nargs='+',  type=validate_paths_arg,
                        help='Paths to text files/folders')

    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')

    args = parser.parse_args()

    tfidf_instance = TFIDF(paths=args.paths)
    tfidf_instance.parse_files()
    tfidf_instance.join_counters()
    tfidf_instance.get_n_max_common(args.max_words)


if __name__ == "__main__":
    main()
