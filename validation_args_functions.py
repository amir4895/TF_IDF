import argparse
from os import path
from tf_idf_logger import LOG


def check_not_neg(value):
    int_value = int(value)
    if int_value <= 0:
        error_msg = f"{value} is a negative value - Invalid"
        LOG.error(error_msg)
        raise argparse.ArgumentTypeError(error_msg)
    return int_value


def validate_paths_arg(arg_path):
    if not path.exists(arg_path):
        error_msg = f"The given path: {arg_path} is invalid\n"
        LOG.error(error_msg)
        raise argparse.ArgumentTypeError(error_msg)
    return arg_path
