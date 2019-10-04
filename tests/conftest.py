import pytest

from tf_idf import TFIDF
from functools import lru_cache
from typing import List, Tuple
from .test_params import generic_tests_params

@pytest.fixture
def tfidf_instance():
    """
    fixture create TFIDF instance with given path set by test params file
    :return: TFIDT instance after analyzing all files and counters
    """
    tfidf_instance = _create_tf_idf_instnace(paths=generic_tests_params['paths'])
    tfidf_instance.parse_files()
    tfidf_instance.join_counters()
    return tfidf_instance


@pytest.fixture
def tfidf_instance_same_paths_twice():
    """
    fixture create TFIDF instance with given path set by test params file
    :return: TFIDT instance after analyzing all files and counters
    """
    tfidf_instance = _create_tf_idf_instnace(paths=generic_tests_params['paths'] + generic_tests_params['paths'])
    tfidf_instance.parse_files()
    tfidf_instance.join_counters()
    return tfidf_instance


@lru_cache()
def _create_tf_idf_instnace(*args, **kwargs):
    kwargs['paths']=kwargs["paths"].split()
    return TFIDF(*args, **kwargs)


def validate_tfidf_res(results: List[Tuple]):

    zipped_results = zip(*results)
    for sub_result in zipped_results:
        words, counters = [], []
        for element in sub_result:
            words.append(element[0])
            counters.append(element[1])
        assert len(set(counters)) == 1, f"The given results are differ"



