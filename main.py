import argparse


def main():
    parser = argparse.ArgumentParser(description='TF_IDF arg parser.')
    parser.add_argument('-N', '--n_max',  type=int, action="store", help='N words with maximal of occurrences',
                        required=True)
    parser.add_argument('-P', '--paths', nargs='+', help='Paths to text files/folders',
                        required=True)
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
